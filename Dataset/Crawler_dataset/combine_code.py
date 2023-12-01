import pandas as pd
import glob
import re
from collections import defaultdict

def combine_excel_files_by_year():
    # 엑셀 파일들이 있는 디렉토리 경로를 지정합니다.
    directory_path = 'Gnews_data_sum/'  # 디렉토리 경로 변경

    # 지정된 디렉토리 내의 모든 엑셀 파일을 찾습니다.
    all_files = glob.glob(directory_path + "news_data_*.xlsx")

    # 연도별 파일 그룹화
    files_by_year = defaultdict(list)
    for filename in all_files:
        year = re.search(r'(\d{4})', filename).group(1)  # 연도 추출
        files_by_year[year].append(filename)

    # 연도별로 파일을 데이터프레임으로 읽어서 합칩니다.
    for year, files in files_by_year.items():
        all_dataframes = []
        for filename in files:
            df = pd.read_excel(filename, index_col=None, header=0)
            all_dataframes.append(df)

        # 모든 데이터프레임을 하나로 합칩니다.
        combined_df = pd.concat(all_dataframes, axis=0, ignore_index=True)

        # 결과를 새로운 엑셀 파일로 저장합니다.
        combined_df.to_excel(f"combined_news_data_{year}.xlsx", index=False)
        print(f"All excel files of {year} have been combined into 'combined_news_data_{year}.xlsx'.")

if __name__ == "__main__":
    combine_excel_files_by_year()