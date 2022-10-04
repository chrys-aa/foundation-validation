import json

apiGatewayResponse = {
    "statusCode": 200,
    "headers" : { "requestId": ""},
    "body": {}
}

response = {
    "recommendation": "MERGE",
    "pr_validation": {
        "DEO4": {
            "identified" : [],
            "validation":[
                
            ]
        },
        "mini-reg": {
            "identified" : "",
            "validation" :[]
        },
        "accessibility": {
            "identified" : "",
            "validation" :[]
        },
    }
}

#Metodos para resposta da lambda
def getResponse():
    apiGatewayResponse["body"] = response
    return apiGatewayResponse

def genericErrorResponse(error):
    apiGatewayResponse["statusCode"] = 500
    apiGatewayResponse["body"] = {"message": str(error) }
    return apiGatewayResponse

def setRequestId(requestId):
    apiGatewayResponse["headers"]["requestId"] = requestId

def errorDEONotFound(deo):
    doNotMerge() 
    validation = {
        "DEO" : deo,
        "status": "FAILED",
        "reasons": ["Número da execução não encontrada no Silk"]
    }
    appendDEOValidation(validation)

def errorMiniNotFound(minireg):
    doNotMerge() 
    validation = {
        "identified": minireg,
        "status": "FAILED",
        "reasons": ["Número da execução não encontrada no Silk"]
        }
    createMiniValidation(validation)

def errorPaccessNotFound(paccess):
    doNotMerge() 
    validation = {
        "identified": paccess,
        "status": "FAILED",
        "reasons": ["Número da execução não encontrada no Silk"]
        }
    createPaccessValidation(validation)

def doNotMerge():
    response["recommendation"] = "DO_NOT_MERGE"

def appendIdentifiedDEOs(deo):
    identified = response["pr_validation"]["DEO4"]["identified"]
    identified.append(deo)

def appendIdentifiedMini(minireg):
    response["pr_validation"]["mini-reg"]["identified"] = minireg

def appendIdentifiedPaccess(paccess):
    response["pr_validation"]["accessibility"]["identified"] = paccess


def appendDEOValidation(validation):
    validationNode = response["pr_validation"]["DEO4"]["validation"]
    validationNode.append(validation)

def createMiniValidation(validation):
    response["pr_validation"]["mini-reg"] = validation

def createPaccessValidation(validation):
    response["pr_validation"]["accessibility"] = validation

def addDEOValidation(deo, reasons):
    if reasons:
        doNotMerge()
        validation = {
        "DEO" : deo,
        "status": "FAILED",
        "reasons": reasons
        }
        appendDEOValidation(validation)
        return
    validation = {
        "DEO" : deo,
        "status": "OK"
        }
    appendDEOValidation(validation)


def addMiniValidation(minireg, reasons):
    if reasons:
        doNotMerge()
        validation = {
            "identified": minireg,
            "status": "FAILED",
            "reasons": reasons
            }
        createMiniValidation(validation)
        return
    validation = {
        "identified": minireg,
        "status": "OK"
        }
    createMiniValidation(validation)

def addPaccessValidation(paccess, reasons):
    if reasons:
        doNotMerge()
        validation = {
            "identified": paccess,
            "status": "FAILED",
            "reasons": reasons
            }
        createPaccessValidation(validation)
        return
    validation = {
        "identified": paccess,
        "status": "OK"
        }
    createPaccessValidation(validation)