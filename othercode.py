a = """
            ventilation = re.findall("Système de ventilation en place\n*(.*)\n",self.text)
            ventilation = ventilation[0]

            chauffage = re.findall("chauffage à (.+?(?=\d))",self.text)
            chauffage = chauffage[0]
            equipementchauffage = re.findall("description\n((.|\n)+?(?=fl))",self.text)
            equipementchauffage = equipementchauffage[0][0].strip()
            equipementchauffage = equipementchauffage.replace("\n"," ")
            eauchaude = re.findall("eau chaude à (.+?(?=\d))",self.text)
            eauchaude = eauchaude[0]

            equipementeauchaude = re.findall("ne Eau chaude sanitaire ((.|\n)+?(?=\n\n\d))",self.text)
            equipementeauchaude= equipementeauchaude[0][0].strip()
            refroidissement = re.findall("refroidissement ((.|\n)*?(?=\d))",self.text)
            refroidissement = refroidissement[0][0].strip()
            eclairage = re.findall("éclairage # ((.|\n)*?(?=\d))",self.text)
            eclairage = eclairage[0][0].strip()
            auxiliaires = re.findall("auxiliaires # ((.|\n)*?(?=\d))",self.text)
            auxiliaires = auxiliaires[0][0].strip()
            """