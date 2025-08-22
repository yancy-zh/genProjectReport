# coding=utf-8
import pandas as pd
from operations.writer import Writer
from operations.reader import Reader
from operations.styler import MyStyler
from operations.validator import Validator


def modifyTables():
    reader = Reader()
    df_subContract = reader.readSubContract()
    df_mainContract = reader.readMainContract()
    df_concat_vertical = pd.concat([df_subContract, df_mainContract])
    df_projs = reader.readProjectReport()
    df_projs_merged = pd.merge(df_concat_vertical, df_projs, on="project_id", how="left")
    df_contracts = reader.readContractReport()
    df_contracts_merged = pd.merge(df_projs_merged, df_contracts, on="contract_id", how="left")
    df_contracts_merged.sort_values(by=['organization', 'department', 'project_id', 'money_flow'],
                                    ascending=[True, True, True, True], inplace=True)


    writer = Writer()
    df_contracts_merged = writer.setGroupId(df_contracts_merged)
    df_reordered = writer.reorderCols(df_contracts_merged)
    writer.writeDataframeToExcel(df_reordered, "df_reordered.xlsx")


def addStyleToTables():
    reader = Reader()
    df = reader.readDataFrame("df_reorderedbk.xlsx")
    mystyler = MyStyler(df)
    mystyler.canNotModifyCols()
    mystyler.highLightProjCategory2()
    mystyler.highlightMoneyFlowIn()
    mystyler.highlightMoneyFlowOut()
    validator = Validator(df)
    indices = validator.projDateValidation()
    mystyler.highLightProjectDateWrong(indices=indices)
    indices_2 = validator.validateMainContractSum()
    mystyler.highLightContractSumInfoWrong(indices_2)
    indices_3 = validator.validateProjNull()
    mystyler.highLightProjNull(indices_3)
    indices_4 = validator.validateDeptName()
    mystyler.highLightDeptRepeat(indices_4)
    indices_5 = validator.validateProjStatus()
    mystyler.highLightProjStatusWrong(indices_5)
    indices_7 = validator.validateProjCategory1()
    mystyler.highLightProjProjSourceWrong(indices_7)
    indices_6 = validator.validateProjNonFirstLine()
    mystyler.highlightProjFirstLine(indices_6)
    sf = mystyler.getStyleFrame()
    writer = Writer()
    # writer.writeStyleFrame(sf)
    writer.writeFinalContractTable(sf)


def modifyProjTable():
    reader = Reader()
    df = reader.readFullProjReport()
    df.sort_values(by=['立项单位', '责任部门', '项目编号'],
                   ascending=[True, True, True], inplace=True)
    validator = Validator(df)
    indices = validator.projDateValidation_1()
    mystyler = MyStyler(df)
    mystyler.highLightProjectDateWrong2(indices)
    sf = mystyler.getStyleFrame()
    mystyler.canNotModifyCols2()
    writer = Writer()
    writer.writeFinalProjTable(sf)

def writeComments():
    writer = Writer()
    writer.writeComments()


if __name__ == '__main__':
    # modifyTables()
    addStyleToTables()
    # writeComments()

