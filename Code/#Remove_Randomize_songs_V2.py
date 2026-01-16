import os
import re

def restore_original_names():
    """
    恢复歌曲的原始文件名
    支持移除以下格式的前缀：
    1. 三位字符前缀：ABC_歌名.mp3（其中ABC可以是字母数字组合）
    2. 单个字母前缀：A_歌名.mp3（兼容旧版本）
    """
    print("正在恢复歌曲的原始文件名...\n")
    
    # 支持的音频格式
    audio_extensions = {'.mp3', '.flac', '.wma', '.m4a', '.wav', '.aac', '.ogg', '.opus'}
    
    restored_count = 0
    skipped_count = 0
    no_prefix_count = 0
    
    # 获取当前目录下的所有文件
    for filename in os.listdir('.'):
        # 检查是否是文件（不是文件夹）
        if not os.path.isfile(filename):
            continue
            
        # 获取文件扩展名
        name_part, ext = os.path.splitext(filename)
        
        # 检查是否是音频文件
        if ext.lower() in audio_extensions:
            # 检查文件名是否包含前缀
            # 模式1：三位字符前缀（字母数字组合 + 下划线）
            # 模式2：单个字母前缀（兼容旧版本）
            
            original_name = None
            
            # 检查是否是三位字符前缀（ABC_...）
            if (len(name_part) >= 4 and 
                name_part[3] == '_' and
                all(c.isalnum() for c in name_part[:3]) and
                name_part[0].isalpha()):
                
                # 提取原始文件名（移除前四个字符：三个字符+下划线）
                original_name = name_part[4:] + ext
            
            # 检查是否是单个字母前缀（A_...） - 兼容旧版本
            elif (len(name_part) >= 2 and 
                  name_part[1] == '_' and 
                  name_part[0].isalpha()):
                
                # 提取原始文件名（移除前两个字符：字母+下划线）
                original_name = name_part[2:] + ext
            
            if original_name:
                # 检查目标文件名是否已存在（避免冲突）
                if not os.path.exists(original_name):
                    # 重命名文件
                    os.rename(filename, original_name)
                    print(f"✓ 恢复: {filename} -> {original_name}")
                    restored_count += 1
                else:
                    print(f"⚠ 跳过（文件已存在）: {filename} -> {original_name}")
                    skipped_count += 1
            else:
                # 没有可识别的前缀
                no_prefix_count += 1
    
    print(f"\n{'='*60}")
    print("恢复完成！")
    print(f"{'='*60}")
    print(f"已恢复: {restored_count} 个文件")
    if skipped_count > 0:
        print(f"跳  过: {skipped_count} 个文件（文件名冲突）")
    print(f"无前缀: {no_prefix_count} 个文件（无需恢复）")
    print(f"{'='*60}")
    
    return restored_count

def main():
    """主函数"""
    print("歌曲文件名恢复工具 v2.0")
    print("=" * 60)
    print("功能：移除音频文件的随机前缀")
    print("支持格式：ABC_歌名.mp3 或 A_歌名.mp3")
    print("-" * 60)
    
    # 询问用户是否继续
    response = input("是否继续恢复原始文件名？(y/n): ").lower()
    if response != 'y' and response != 'yes':
        print("操作已取消。")
        return
    
    # 执行恢复操作
    try:
        restored = restore_original_names()
        
        if restored > 0:
            print("\n💡 提示：")
            print("1. 如果部分文件未能恢复，可能是因为目标文件名已存在")
            print("2. 你可以手动重命名这些文件")
            print("3. 如果仍有前缀未移除，可能是前缀格式不匹配")
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        print("请检查是否有文件正在被其他程序使用。")
    
    # 等待用户按Enter键退出
    input("\n按Enter键退出...")

if __name__ == "__main__":
    main()