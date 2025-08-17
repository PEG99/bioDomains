import pandas as pd
import os

def merge_3zm_excel_files():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 合并后的数据列表
    merged_data = []
    
    # 遍历3zm1.xlsx到3zm9.xlsx文件
    for i in range(1, 10):
        filename = f'3zm{i}.xlsx'
        filepath = os.path.join(current_dir, filename)
        
        if os.path.exists(filepath):
            try:
                # 读取Excel文件
                df = pd.read_excel(filepath)
                
                # 检查是否有A列数据
                if not df.empty and len(df.columns) > 0:
                    # 提取A列数据（第一列）
                    column_a = df.iloc[:, 0]
                    
                    # 过滤掉空值
                    column_a = column_a.dropna()
                    
                    # 添加到合并数据中
                    merged_data.extend(column_a.tolist())
                    
                    print(f'已处理 {filename}，提取了 {len(column_a)} 行数据')
                else:
                    print(f'{filename} 文件为空或没有数据')
                    
            except Exception as e:
                print(f'处理 {filename} 时出错: {str(e)}')
        else:
            print(f'文件 {filename} 不存在')
    
    # 创建合并后的DataFrame
    if merged_data:
        merged_df = pd.DataFrame(merged_data, columns=['A列数据'])
        
        # 保存到新的Excel文件
        output_filename = '3zm_merged.xlsx'
        merged_df.to_excel(output_filename, index=False)
        
        print(f'\n合并完成！共合并了 {len(merged_data)} 行数据')
        print(f'输出文件: {output_filename}')
    else:
        print('没有找到有效数据进行合并')

if __name__ == '__main__':
    merge_3zm_excel_files() 