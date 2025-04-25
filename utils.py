
def getProccessedPdfs(ws):
    L = []
    for i in range(3,ws.max_row +1):
        L.append(ws[f"A{i}"].value)
    return L

