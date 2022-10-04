import datetime
import silk_requester
import response_creator

# 15 days ago global var used to validate DEO and accessibility expire
_EXPIRE_DATE = datetime.datetime.now() - datetime.timedelta(days=15)
print(f'Data de validade considerada para Acessibilidade: {_EXPIRE_DATE} // {int(_EXPIRE_DATE.timestamp())}')

def processPaccess(pAccess, release_number):
    print(f'Processando Parecer de Accessibilidade {pAccess}')
    response_creator.appendIdentifiedPaccess(pAccess)
    reasons = []
    execution = silk_requester.getExecutionInfo(pAccess)

    if not execution:
        response_creator.errorPaccessNotFound(pAccess)
        return

    executionName = execution[0]['executionPlanName']
    if release_number not in executionName:
        reasons.append("Versão da release não identificada no nome da execução")

    if "acessibilidade" not in executionName:
        reasons.append("Tag acessibilidade não identificada no nome da execução")

    time = datetime.datetime.fromtimestamp(execution[0]["startTime"] / 1e3)
    if  time < _EXPIRE_DATE:
        reasons.append("Execução com data de execução expirada, deve ser no máximo D-15")

    if execution[0]["status"] == "FAILED":
        reasons.append("Contém testes que falharam na execução")
    
    if execution[0]["status"] == "NOT_EXECUTED":
        reasons.append("Contém testes não executados")
    
    response_creator.addPaccessValidation(pAccess, reasons)