import re

def extractDEOs(pr_body):
    DEO4Regex = re.search(r"<DEO4>(.*)</DEO4>", pr_body).group(1)
    print(f"DEOs identificados no PR: {DEO4Regex}")
    return DEO4Regex.split(";")

def extractMinireg(pr_body):
    miniregRegex = re.search(r"<MINIREG>(.*)</MINIREG>", pr_body).group(1)
    print(f"mini-regressivo identificados no PR: {miniregRegex}")
    return miniregRegex

def extractPAccess(pr_body):
    pAccessRegex = re.search(r"<PACESS>(.*)</PACESS>", pr_body).group(1)
    print(f"Parecer de acessibilidade identificados no PR: {pAccessRegex}")
    return pAccessRegex
