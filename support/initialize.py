import os
def initialize():
    tmppath = "tmp"
    reportpath="reports"
    isTmpExist = os.path.exists(tmppath)
    isReportExist = os.path.exists(reportpath)
    # check if tmp folder exist
    if not isTmpExist:
        # if not create
        os.makedirs(tmppath)
    else:
        # if exist clear tmp files
        for f in os.listdir(tmppath):
            os.remove(os.path.join(tmppath, f))
    # check if reports folder exist
    if not isReportExist:
        os.makedirs(reportpath)
    