import pandas as pd
import os

def sort_kyym_domains():
    # 获取当前目录
    current_dir = os.getcwd()
    filename = 'kyym.xlsx'
    filepath = os.path.join(current_dir, filename)
    
    if not os.path.exists(filepath):
        print(f'文件 {filename} 不存在')
        return
    
    try:
        # 读取Excel文件
        print(f'正在读取 {filename}...')
        df = pd.read_excel(filepath)
        
        # 检查是否有A列数据
        if df.empty or len(df.columns) == 0:
            print('文件为空或没有数据')
            return
        
        # 提取A列数据（第一列）
        column_a = df.iloc[:, 0]
        
        # 过滤掉空值
        column_a = column_a.dropna()
        
        print(f'原始数据：{len(column_a)} 行')
        
        # 显示前10个域名作为示例
        print('\n排序前的示例（前10个）：')
        for i, domain in enumerate(column_a.head(10)):
            print(f'{i+1}. {domain}')
        
        # 对域名进行排序
        print('\n正在排序...')
        sorted_domains = sorted(column_a.tolist())
        
        # 显示排序后的前10个域名
        print('\n排序后的示例（前10个）：')
        for i, domain in enumerate(sorted_domains[:10]):
            print(f'{i+1}. {domain}')
        
        # 创建排序后的DataFrame
        sorted_df = pd.DataFrame(sorted_domains, columns=['排序后域名'])
        
        # 保存到新的Excel文件
        output_filename = 'kyym_sorted.xlsx'
        sorted_df.to_excel(output_filename, index=False)
        
        print(f'\n排序完成！')
        print(f'共处理了 {len(sorted_domains)} 个域名')
        print(f'输出文件: {output_filename}')
        
        # 显示排序统计信息
        print(f'\n排序统计：')
        print(f'第一个域名: {sorted_domains[0]}')
        print(f'最后一个域名: {sorted_domains[-1]}')
        
    except Exception as e:
        print(f'处理文件时出错: {str(e)}')

if __name__ == '__main__':
    sort_kyym_domains() 