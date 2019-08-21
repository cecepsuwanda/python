

class mhs:
    def __init__(self,lst):
        for key in lst:
            setattr(self,key,lst[key])

class mtk:
    def __init__(self,lst):
        for key in lst:
            setattr(self,key,lst[key])            
 
def tb_mhs_to_lst_obj_mhs(data):
    return mhs(data)

def tb_mtk_to_lst_obj_mtk(data):
    return mtk(data)

def baca_tb(tb,callback):
    hsl=[]
    for row in tb:
        hsl.append(callback(row)) 
    return hsl    



if __name__ == '__main__':
   tb_mhs = [{ 'nim' : '01' ,'nama' :'agus' },{ 'nim' : '02' ,'nama' :'hendra' } ]
   tb_mtk = [{ 'kode' : '01' ,'nama' :'mtk1' },{ 'kode' : '02' ,'nama' :'mtk2' } ]
   tb_nilai = [{'nim':'01','kode':'01','HM':'A'},
               {'nim':'01','kode':'02','HM':'B'},
               {'nim':'02','kode':'01','HM':'A'},
               {'nim':'02','kode':'02','HM':'A'}]

   lst_obj_mhs=baca_tb(tb_mhs,tb_mhs_to_lst_obj_mhs)
   print(lst_obj_mhs[0].__dict__)
   lst_obj_mtk=baca_tb(tb_mtk,tb_mtk_to_lst_obj_mtk)
   print(lst_obj_mtk[0].__dict__)
