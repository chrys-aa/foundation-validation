import datetime
import silk_requester
import response_creator

# constants
_QTD_TESTS_MINIREG = 2

# 48h ago global var used to validate mini expire
_EXPIRE_DATE = datetime.datetime.now() - datetime.timedelta(hours=48)
print(f'Data de validade considerada para mini: {_EXPIRE_DATE} // {int(_EXPIRE_DATE.timestamp())}')

def processMinireg(minireg, release_number):
    print(f'Processando Mini {minireg}')
    response_creator.appendIdentifiedMini(minireg)
    reasons = []
    execution = silk_requester.getExecutionInfo(minireg)

    if not execution:
        response_creator.errorMiniNotFound(minireg)
        return

    executionName = execution[0]['executionPlanName']
    if release_number not in executionName:
        reasons.append("Versão da release não identificada no nome da execução")

    time = datetime.datetime.fromtimestamp(execution[0]["startTime"] / 1e3)
    if  time < _EXPIRE_DATE:
        reasons.append("Execução com data de execução expirada, deve ser no máximo D-2")
        
    if execution[0]["status"] == "FAILED":
        reasons.append("Contém testes que falharam na execução")
    
    if execution[0]["status"] == "NOT_EXECUTED":
        reasons.append("Contém testes não executados")

    detailedExecution = silk_requester.getExecutionDetail(minireg)
    miniregTests = len(detailedExecution)

    if miniregTests != _QTD_TESTS_MINIREG:
        reasons.append(f"O plano do mini-regressivo deve conter {_QTD_TESTS_MINIREG} testes.")

    response_creator.addMiniValidation(minireg, reasons)