#1-function
def info(ism,yosh,yjoy,level):
    new = {
        'ism':ism,
        'yosh':yosh,
        'yjoy':yjoy,
        'level':level
        }
    return new

#2-function
def student_kirit():
    print('Yangi o\'quvchi haqida ma\'lumotlarni kiriting!')
    student = []
    while True:
        ism = input('O\'quchi ismini kiriting: ')
        yosh = input('O\'quchi yoshini kiritiing: ')
        yjoy = input('O\'quchi yashash joyini kiriting: ')
        level = input('O\'quchi darajasini kiriting: ')
        student.append(info(ism,yosh,yjoy,level))
        add = input('Yana yangi o\'quvchi bormi? (xa/yo\'q):')
        if add != 'xa':
            break
#3-function    
def info_print(info):
    print(f" Ism:{info['ism'].title()}\n",
          f"Yosh:{info['yosh']}\n",
          f"Yashash joyi:{info['yjoy'].title()}\n",
          f"Tilni bilish darajasi:{info['level'].upper()}\n")