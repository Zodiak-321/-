import os
import random
import string

def add_random_prefix():
    """
    为歌曲添加随机三位字符前缀（格式：ABC_歌名）
    第一位：大写字母 A-Z
    第二、三位：大写字母或数字 0-9
    """
    print("正在为歌曲添加随机三位字符前缀（格式：ABC_歌名）...\n")
    
    # 支持的音频格式
    extensions = {'.mp3', '.flac', '.wma', '.m4a', '.wav', '.aac', '.ogg', '.opus'}
    
    count = 0
    skipped = 0
    
    # 获取当前目录所有音频文件
    audio_files = []
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            name, ext = os.path.splitext(filename)
            if ext.lower() in extensions:
                audio_files.append((filename, name, ext))
    
    # 打乱文件列表顺序，确保真正的随机性
    random.shuffle(audio_files)
    
    for filename, name, ext in audio_files:
        # 检查是否已经有三位字符前缀（格式：ABC_...）
        # 三个字符可以是字母或数字，第四个字符必须是下划线
        if len(name) >= 4 and name[3] == '_':
            # 检查前三个字符是否都是合法字符（字母或数字）
            if all(c.isalnum() for c in name[:3]) and name[0].isalpha():
                print(f"跳过（已有前缀）: {filename}")
                skipped += 1
                continue
        
        # 生成随机前缀
        # 第一位：大写字母
        first_char = random.choice(string.ascii_uppercase)
        
        # 第二、三位：大写字母或数字
        chars_pool = string.ascii_uppercase + string.digits
        second_char = random.choice(chars_pool)
        third_char = random.choice(chars_pool)
        
        prefix = f"{first_char}{second_char}{third_char}"
        new_name = f"{prefix}_{filename}"
        
        # 重命名文件
        try:
            os.rename(filename, new_name)
            print(f"重命名: {filename} -> {new_name}")
            count += 1
        except Exception as e:
            print(f"错误: 无法重命名 {filename}: {e}")
    
    print(f"\n完成！")
    print(f"成功重命名: {count} 个文件")
    print(f"跳    过: {skipped} 个文件（已有前缀）")
    
    return count

def main():
    """主函数"""
    print("歌曲随机前缀生成器 v2.0")
    print("=" * 60)
    print("功能：为歌曲添加三位随机字符前缀（格式：ABC_歌名）")
    print("字符范围：第一位A-Z，第二三位A-Z或0-9")
    print("总计可能性：36 × 36 × 36 = 46,656 种组合")
    print("-" * 60)
    
    # 询问用户是否继续
    response = input("是否开始添加随机前缀？(y/n): ").lower()
    if response != 'y' and response != 'yes':
        print("操作已取消。")
        return
    
    # 显示警告信息
    print("\n⚠️  注意：此操作将修改文件名")
    print("   建议先备份重要文件！")
    confirm = input("是否继续？(y/n): ").lower()
    if confirm != 'y' and confirm != 'yes':
        print("操作已取消。")
        return
    
    # 执行添加前缀操作
    try:
        add_random_prefix()
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        print("请检查是否有文件正在被其他程序使用。")
    
    # 等待用户按Enter键退出
    input("\n按Enter键退出...")

if __name__ == "__main__":
    main()