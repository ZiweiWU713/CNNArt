import os
import csv

class DatabaseInfo:

    sPathOut = '' # set output path for results
    sDatabase = ''
    sSubDirs = ''
    sPathIn = ''
    lPats = ''
    lImgData = '' # list of imaging data

    def __init__(self,sDatabase = None,sSubDirs = None):
        if sDatabase is None:
            self.sDatabase = 'MRPhysics'
        else:
            self.sDatabase = sDatabase

        if sSubDirs is None:
            self.sSubDirs = ['newProtocol','dicom_sorted'] # name of subdirectory in [database, patient]
        else:
            self.sSubDirs = sSubDirs

        self.sPathIn = '/med_data/ImageSimilarity/Databases' + os.sep + self.sDatabase + os.sep + self.sSubDirs[0]
        # parse patients
        self.lPats = [name for name in os.listdir(self.sPathIn) if os.path.isdir(os.path.join(self.sPathIn, name))]

        # parse config file (according to set database) => TODO (TK): replace by automatic parsing in directory
        ifile=open('config'+os.sep+self.sDatabase+'Database.csv',"rb") # config file must exist for database!
        reader = csv.reader(ifile)
        lImgData = [MRData(rows[0],rows[1],rows[2],rows[3]) for rows in reader]
        ifile.close()

    def get_mrt_model(self):
        #{key: value for key, value in A.__dict__.items() if not key.startswith('__') and not callable(key)}
        return {item.sPath:item.sNumber for item in self.lImgData}

    def get_mrt_smodel(self):
        return {item.sPath: item.sBodyregion for item in self.lImgData}

    def get_mrt_artefact(self):
        return {item.sPath: item.sArtefact for item in self.lImgData}
