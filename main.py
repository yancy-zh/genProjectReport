# coding=utf-8
import pandas as pd
from operations.writer import Writer
from operations.reader import Reader


def modifyTables():
    reader = Reader()
    df_subContract = reader.readSubContract()
    df_mainContract = reader.readMainContract()
    df_concat_vertical = pd.concat([df_subContract, df_mainContract])
    df_projs = reader.readProjectReport()
    df_projs_merged = pd.merge(df_concat_vertical, df_projs, on="project_id", how="left")
    df_contracts = reader.readContractReport()
    df_contracts_merged = pd.merge(df_projs_merged,df_contracts, on="contract_id", how="left")
    df_contracts_merged.sort_values(by = ['organization', 'department', 'project_id','money_flow'], ascending=[True,True,True,True],inplace=True)
    writer = Writer()
    df_reordered= writer.reorderCols(df_contracts_merged)
    if df_reordered is not None:
        writer.writeFinalTable(df_reordered)

if __name__ == '__main__':
    modifyTables()
