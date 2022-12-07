import base64
def getBase64EncodedImage(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        encoded_string = encoded_string.decode()
    return encoded_string

def saveHtmlReport(har,reportedRequests,filterReqUrl,timetoload,imageData,projectName):
    harData=har
    harEntries=harData['log']['entries']
    filteredEntries=[d for d in harEntries if (d['request']['method'] in reportedRequests and filterReqUrl in d['request']['url'])]
    sortedEntries=sorted(filteredEntries, key=lambda d: d['time']) 
    sortedEntries.reverse()
    # harData['log']['entries']=sortedEntries
    projectFileName=projectName.replace(" ", "_")

    # sampleImage=getBase64EncodedImage(f'./sample_images/{imageData}')
    initialImage=getBase64EncodedImage(f'./tmp/{projectFileName}_initial.png')
    finallImage=getBase64EncodedImage(f'./tmp/{projectFileName}_final.png')
    

    timeinMs=int(timetoload.total_seconds() * 1000)
    # generate table data
    tableData=''
    for x in sortedEntries:
        tableData+=f'''
            <tr>
                <td>{x['request']['url']}</td>
                <td>{x['request']['method']}</td>
                <td>{x['response']['status']}</td>
                <td>{x['time']}</td>
            </tr>
        '''
    html=f'''<!DOCTYPE html>
            <html>
            <head>
                <title>{projectName}</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <!-- Bootstrap -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            </head>
            <body>
                <div class="row col-12 d-flex justify-content-center my-5">
                <div class="col-6 d-flex flex-column justify-content-center align-items-center">
                    <h1>{projectName}</h1>
                    <span>It took</span>
                    <span><strong>{timeinMs}</strong> milliseconds</span>
                    <span>to load the below component</span>
                    <div class="row col-12 d-flex justify-content-center">
                        <img src="data:image/png;base64,{initialImage}" class="img-fluid col-6" alt="initial">
                        <img src="data:image/png;base64,{finallImage}" class="img-fluid col-6" alt="final">
                    </div>
                
                <div class="col-12 d-flex flex-column justify-content-center align-items-start mt-2">
                    <h2>Requests:</h2>
                    <div class="col-12 my-1">
                    <table class="table">
                    <thead>
                        <tr>
                        <th scope="col">Url</th>
                        <th scope="col">Method</th>
                        <th scope="col">Status</th>
                        <th scope="col">Time(ms)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {tableData}
                    </tbody>
                    </table>
                    </div>
                    <div class="col-12">
                        <small>Note: This is a filtered list. You can view the full data from {"./reports/"+projectFileName+"_full_har.json"}</small>
                    </div>
                </div>
                
            </body>
            </html>
            '''
    f = open("./reports/"+projectFileName+".html", "w")
    f.write(html)
    f.close()
    print('Time to load was')
    print(timetoload)
