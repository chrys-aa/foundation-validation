import datetime
import silk_requester
import response_creator


# 15 days ago global var used to validate DEO and accessibility expire
_EXPIRE_DATE = datetime.datetime.now() - datetime.timedelta(days=15)
print(f'Data de validade considerada para DEOs: {_EXPIRE_DATE} // {int(_EXPIRE_DATE.timestamp())}')



def processDEOs(deos, release_number):
    for deo in deos:
        reasons = []
        print(f'Processando DEO {deo}')
        execution = silk_requester.getExecutionInfo(deo)
        response_creator.appendIdentifiedDEOs(deo)
        if not execution:
            response_creator.errorDEONotFound(deo)
            continue
        executionName = execution[0]['executionPlanName']
        if release_number not in executionName:
            reasons.append("Versão da release não identificada no nome da execução")

        time = datetime.datetime.fromtimestamp(execution[0]["startTime"] / 1e3)
        if  time < _EXPIRE_DATE:
            reasons.append("Execução com data de execução expirada, deve ser no máximo D-15")

        if execution[0]["status"] == "FAILED":
            reasons.append("Contém testes que falharam na execução")
        
        if execution[0]["status"] == "NOT_EXECUTED":
            reasons.append("Contém testes não executados")

        response_creator.addDEOValidation(deo, reasons)
        