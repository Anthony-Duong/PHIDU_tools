# https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files
import pandas as pd
import geopandas as gpd

class AUS_geo():
    def __init__(self):
        self.shapedata = gpd.read_file('boundary_data\LGA_2023_AUST_GDA2020.shp')
        #self.plot_data = plot_data
        
    def state(self,state_abr):
        state_code = { # dictionary translating state abriviations to codes
            'NSW' : '1',
            'VIC' : '2',
            'QLD' : '3',
            'SA' : '4',
            'WA' : '5',
            'TAS' : '6',
            'NT' : '7',
            'ACT' : '8',
            'OT' : '9',
        }

        # code to allow for selction of multiple states
        query = [] #query list
        [query.append(state_code[i]) for i in state_abr] #adds state codes from dictionary to query list
        return self.shapedata[self.shapedata['STE_CODE21'].isin(query)]
        
    def PHN(self,PHN_code):
        PHN_LGA = { # dictionary listing PHNs and their composite LGAs
            '101': (['10500','11300','11520','11570a','12930','14170','16550','17100','17150','17200','18050','18500','19399a']),
            '102' : (['14000','14100','14500','14700','15350','15950','15990','16260a','16700','18250']),
            '103' : (['10750','12380','16260b','17420']),
            '104' : (['10900','13800','14870','16350']),
            '105' : (['11450','11500','11570b','12850','14900','18350','18400']),
            '106' : (['10550','12750','13310','14400','16490','16900','16950','17040','17640','18450','18710']),
            '107' : (['10300','10470','10850','10950','11150','11200','11250','11400','11700','11750','12150','12350','12390','12900','12950','14600a','15270','15850','16100','16150','16200','17900','17950','18020','18100','18200','19399b']),
            '108' : (['10180','11650','11720','12700','13010','13550','13660','14220','14650','14920','15050','15240','15300','15650','15750','15900','16400','17000','17310','17400a','17620','17650','17850']),
            '109' : (['10250','10600','11350','11730','11800','14350','14550','14850','15700','16380','16610','17400b','17550']),
            '110' : (['10650','10800','11600','12000','12160','12730','12870','13340','13450','13850','13910','14300','14600b','14750','14950','15520','15560','15800','17080','17350','17750']),
            '201' : (['21180','21890','23110','23270','24130a','24330','24600','24650','25060','25150a','25250','27260','27350']),
            '202' : (['20660','21110','23670','24210','24410','24850a','24970a','25620a','25710','26980','27070','27450']),
            '203' : (['20910','21450','21610','22170','22310','22670','23430','24970b','25340','25900','26350']),
            '204' : (['20740','20830','22110','23810','26170','26810','29399a']),
            '205' : (['10050','20110','21010','21270','21370','22250','22620','22830','23350','23940a','24130b','24250','24780','24850b','24900','25430','25620b','26430','26610','26670','26700','27170','29399b']),
            '206' : (['20260','20570','21670','21750','21830','22410','22490','22750','22910','22980','23190','23940b','25150b','25490','25810','25990','26080','26260','26490','26730','26890','27630']),
            '301' : (['31000a','35010','36580a']),
            '302' : (['31000b','34590','36250','36510a']),
            '303' : (['33430','36510b']),
            '304' : (['30370a','32330','33610','33960','34580','36510c','36580b','36630','36660','36910','37310']),
            '305' : (['30300','30410','30450','30760','30900','31750','31950','32250','32450','32750','32770','34710','34800','34860','35250','35300','35600','35800','36150','37400']),
            '306' : (['30370b','31820','32270','33220','33360','33620','34530','35740','35760','36370','36720','37550']),
            '307' : (['30250','31900','32080','32260','32310','32500','32600','32810','33100','33200','33800','33830','33980','34420','34570','34770','34830','34880','35670','35780','35790','36070','36300','36820','36950','36960','37010','37300','37340','37570','37600']),
            '401' : (['40070','40700','40910','41060','42600','44060','44340','45290','45340','45680','45890','46510','47140','47700','47980','48260','48410']),
            '402' : (['40120','40150','40220','40250','40310','40430','40520','41010','41140','41190','41330','41560','41750','41830','41960','42030','42110','42250','42750','43080','43220','43360','43650','43710','43790','44000','44210','44550','44620','44830','45040','45090','45120','45400','45540','46090','46300','46450','46670','46860','46970','47290','47490','47630','47800','47910','48050','48130','48340','48540','48640','48750','48830','49399']),
            '501' : (['50350','50420','51310','51750','52170','54170','54200','55740','56090','56580','56930','57080','57910','57980','58050','58570','58760']),
            '502' : (['50210','50490','51330','51820','53150','53430','53780','54830','55110','55320','56230','57490','57700','57840','58510','58820']),
            '503' : (['50080','50250','50280','50560','50630','50770','50840','50910','50980','51080','51120','51190','51260','51400','51470','51540','51610','51680','51890','51960','52030','52100','52240','52310','52380','52450','52520','52590','52660','52730','52800','52870','52940','53010','53080','53220','53290','53360','53570','53640','53710','53800','53920','53990','54060','54130','54280','54310','54340','54410','54480','54550','54620','54690','54760','54900','54970','55040','55180','55250','55390','55460','55530','55600','55670','55810','55880','55950','56160','56300','56370','56460','56620','56730','56790','56860','57000','57140','57210','57280','57350','57420','57630','57770','58190','58260','58330','58400','58470','58540','58610','58680','58890','59030','59100','59170','59250','59310','59320','59330','59340','59350','59360','59370']),
            '601' : (['60210','60410','60610','60810','61010','61210','61410','61510','61610','61810','62010','62210','62410','62610','62810','63010','63210','63410','63610','63810','64010','64210','64610','64810','65010','65210','65410','65610','65810']),
            '701' : (['70200','70420','70540','70620','70700','71000','71150','71300','72200','72300','72330','72800','73600','74050','74550','74560','74660','74680','79399']),
            '801' : (['89399'])
        }
        # code to allow for selction of multiple PHNs
        query = [] #query list
        [query.extend(PHN_LGA[i]) for i in PHN_code] #adds LGA codes from dictionary to query list
        return self.shapedata[self.shapedata['LGA_CODE23'].isin(query)]
        
    def LGA(self,LGA_code):
        return self.shapedata[self.shapedata['LGA_CODE23'].isin(LGA_code)]
    
    def choropleth(self):
        pass