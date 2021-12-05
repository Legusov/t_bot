
import telebot
import sqlite3
from telebot import types
import pathlib, urllib.request, re
from pathlib import Path

user_n = ''
name = ''
rename = ''
tmp_name = ''
rename_stop = 0
start_mid = ''
keydel = 0
tema_testa = []
tema_inf = []
test = []
btn = []
tema = ''
test_key = []
n_t_key = []
answer = []
i_quest = 0
i_tema = ''
num_id = 0
it = 0
i = 0
iA = 0
key_end = 0
rezult = 0
mes_del  = 0
n_test = ['1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣','🔟']
number_test = []
history = ''
new_test = 0
final_test = 0
first_msg = 0
tema_msg = 0
vopr_po_teme = 0
tema_v_vopr = 0
var_otv_msg = 0
vopr_mes = 0
rez_msg = 0
no_reg = 0
key_reg = 0
id_mes_nema =[]
msg_vozvrat = 0
n_bd = ''
by_msg = 0
re_reg = 0
noreg_msg = 0
name_bd = ''
surname = ''
service = ''
tabn = ''
res = ''
txt = "bd.txt"

bot = telebot.TeleBot("")
# сброс переменных
def all_sbros():
    global name,rename,tmp_name,rename_stop,start_mid,keydel,tema_testa,tema_inf,test,btn,tema,test_key,n_t_key,answer,i_quest,i_tema,num_id,it,i,iA,key_end,n_test,number_test,rezult, rezult100, itog_proc
    name = ''
    rename = ''
    tmp_name = ''
    rename_stop = 0
    start_mid = ''
    keydel = 0
    tema_testa = []
    tema_inf = []
    test = []
    btn = []
    tema = ''
    test_key = []
    n_t_key = []
    answer = []
    i_quest = 0
    i_tema = ''
    num_id = 0
    it = 0
    i = 0
    iA = 0
    key_end = 0
    n_test = ['1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣','🔟']
    number_test = []
    rezult = 0
    rezult100 = 0
#фильтрация и преобразование Инфррмационная безопасность/ИБ и пр. в тестах
def file_r_w(str_line):
    global txt
    try:
        f = open(txt)
    except IOError as e:
        #print(u'Файл не существует, создаем ',txt)
        f = open(txt, 'w')
    else:

        with f:
            if str_line[0] == "T":
                str_line = str_line.replace("информационной безопасности", "ИБ")
                str_line = str_line.replace(" и продукты", "")
                str_line = str_line.replace("антивируса", "ПО")

            str_line = str_line.replace("информационной безопасности", "ИБ")
            str_line = str_line.replace("информационная безопасность", "ИБ")

            f = open(txt, 'a')
            if str_line[-1] == '+':
                str_line = str_line[:-1]+" +"
                f.write(str_line.replace('* ', '*')+"\n")
            elif  str_line[-1] == '-':
                str_line = str_line[:-1]+" -"
                f.write(str_line.replace('* ', '*')+ "\n")
            else:
                f.write(str_line.replace('* ','*')+ " \n")
            f.close()


    return
# подготовка тем теста
def read_line(str_line,tema):
    global answer, n_t_key, txt
    if tema == None:
        f = open(txt, "r")
        outline = []
        while True:
            line = f.readline()
            if not line:
                break
            if str_line == line[0]:
                readline = "".join(re.findall("_.*\*(.*)", str(line)))
                outline.append(readline)
        f.close()
    elif tema != None:
        f = open(txt, "r")
        outline = []
        key_test = 0
        while True:
            line = f.readline()
            if not line:
                break
            if key_test == 1 and line[0] == "T":
                key_test = 0
                break
            if tema == "".join(re.findall("_.*\*(.*)", str(line))):
                key_test = 1
            if line[0]==str_line and key_test == 1 :
                readline = "".join(re.findall("_.*\*(.*)", str(line)))
                n_t_key.append("".join(re.findall("_(.*)\*.*", str(line))))
                outline.append(readline)
        f.close()

    return outline
#парсинг тестов
def create_test():
    global txt

    url = 'https://eljob.ru/'
    link = urllib.request.urlopen(url)
    lines_url = []
    K_numb = 0
    K_numb += 1
    for line in link.readlines():
        lines_url.append(line)
        category = "".join(re.findall('.*/category/(\d+).*Безоп.*', line.decode('utf-8')))
        #print(line.decode('utf-8'))
        if category != "":
            T_numb = 0
            K="К_numb-"+str(K_numb)+"*"+"".join(re.findall('.*/category/\d+.*>(.*Безоп.*)<', line.decode('utf-8')))
            file_r_w(K)
            #print("К-"+"".join(re.findall('.*/category/\d+.*>(.*Безоп.*)<', line.decode('utf-8')) ))
            url_course = 'https://eljob.ru/category/'+str(category)
            link_course = urllib.request.urlopen(url_course)
            lines_course = []

            for line_course in link_course.readlines():
                lines_course.append(line_course)
                tema = "".join(re.findall('.*/course/(\d+)\S*>.*информац.*безо.*<', line_course.decode('utf-8')))
                if tema != "":
                    T_numb += 1
                    t_numb = 0
                    T="T_numb-"+str(K_numb)+"-"+str(T_numb)+"*"+"".join(re.findall('.*/course/\d+\S*>(.*информац.*безо.*)<', line_course.decode('utf-8')))
                    file_r_w(T)

                    #print("T-"+"".join(re.findall('.*/course/\d+\S*>(.*информац.*безо.*)<', line_course.decode('utf-8'))))
                    url_tema = 'https://eljob.ru/course/' + str(tema)
                    link_tema = urllib.request.urlopen(url_tema)
                    lines_test = []
                    i = 1

                    for line_tema in link_tema.readlines():
                        lines_test.append(line_tema)
                        test = "".join(re.findall('.*/test/([0-9_]*)', line_tema.decode('utf-8')))
                        if test != "":
                            t_numb += 1
                            A_numb = 0
                            Q_numb = 0
                            #print("test "+test)
                            #print("Тест - " + "".join(re.findall('.*/test/[0-9_]*.*>(.*)<', line_tema.decode('utf-8'))))
                            t="t_numb-"+str(K_numb)+"-"+str(T_numb)+"-"+str(t_numb)+"*Тест "+str(i)
                            file_r_w(t)
                            #print("t-Тест",i)
                            i+=1
                            url_test = 'https://eljob.ru/test/' + str(test)
                            link_test = urllib.request.urlopen(url_test)
                            lines_question = []
                            line_quest_old = ""
                            j = 1
                            for line_quest in link_test.readlines():
                                #lines_question.append(line_quest)
                                line_true = line_quest_old
                                line_quest_old = line_quest
                                #number = "".join(re.findall('.*Номер (\d+)', line_quest.decode('utf-8')))
                                #if number != "" :
                                    #print('\n')
                                    #print("Q-Вопрос", j)
                                    #j+=1
                                #test = "".join(re.findall(r'<pre class="title">(.*)<', find)).replace('"', '')
                                quest = "".join(re.findall(r'<pre class="title">(.*\??:?)<?', line_quest.decode('utf-8'))).replace('</pre>','')
                                if quest != "" :
                                    A_numb += 1
                                    Q_numb += 1
                                    Q="Q_numb-"+str(K_numb)+"-"+str(T_numb)+"-"+str(t_numb)+"-"+str(Q_numb)+"*"+quest
                                    file_r_w(Q)
                                    #print("Q-"+quest)
                                table_str = "".join(re.findall(r'<table><tr><td>(.*)?</', line_quest.decode('utf-8')))
                                if table_str != "":
                                    Q1_str = "Q_numb-" + str(K_numb) + "-" + str(T_numb) + "-" + str(t_numb) + "-" + str(
                                        Q_numb) + "*"
                                    pat = re.compile(r'(</tr>|</td>|</table>)')
                                    table = re.sub(pat, "", table_str).replace('<tr>', '\n'+Q1_str).replace('<td>', ' ').replace('  ',' ')
                                    Q2="Q_numb-"+str(K_numb)+"-"+str(T_numb)+"-"+str(t_numb)+"-"+str(Q_numb)+"*" + " " + table
                                    file_r_w(Q2)
                                    #print("Q-"+table)
                                answer = "".join(re.findall(r'<strong>\((\d)\)', line_quest.decode('utf-8')))+\
                                         "".join(re.findall(r'</strong(>.*)&nbsp', line_quest.decode('utf-8'))).replace(">", '. ')
                                if answer != "":
                                    if re.search('<div class="title correct">', line_true.decode('utf-8')) :
                                        A1="A_numb-"+str(K_numb)+"-"+str(T_numb)+"-"+str(t_numb)+"-"+str(A_numb)+"*"+answer+"+"
                                        file_r_w(A1)
                                        #print("A-"+answer, "+")
                                    else:
                                        A2 = "A_numb-"+str(K_numb)+"-"+str(T_numb)+"-"+str(t_numb)+"-"+str(A_numb)+"*" + answer + "-"
                                        file_r_w(A2)
                                        #print("A-"+answer, "-")
                            link_test.close()
                    link_tema.close()
            link_course.close()
    link.close()
# поиск темы на сайте по шаблону
def search_test():
    global test,tema_testa, tema_inf, txt
    tema_testa = []
    url_cat = "https://eljob.ru/"
    url_course = url_cat+'course/'
    urt_test = ''
    url_in = url_cat+"category/9"
    link = urllib.request.urlopen(url_in)
    lines = []
    tema_len = 0
    i = 0
    for line in link.readlines():
        lines.append(line)
        #print (line.decode('utf-8'))
        tema = "".join(re.findall('/course/\d+\S*>(.*информац.*безо.*)<', line.decode('utf-8')))
        if "." in tema:
            tema = "".join(re.findall('(.*)\.', tema))
        tema = tema.replace("информационной безопасности", "ИБ")
        tema = tema.replace(" и продукты", "")
        tema = tema.replace("антивируса", "ПО")
        if tema != "":

            #print(tema)
            if tema_len < len(tema):
                tema_len = len(tema)
            tema_testa.append(tema)

            link.close()
    link.close()

    tema_testa.sort(key=len)
    while i < len(tema_testa):
        tema_testa[i] = str(number_test[i]) + " " + tema_testa[i]
        i+=1
        tema_inf.append('Материал по теме "Основы ИБ"\n https://telegra.ph/Osnovy-informacionnoj-bezopasnosti-11-24')
    return tema_testa
# формирование списка тестов
def out_test(message):
    global tema, test_key, number_test, n_t_key, key_end, tema_msg, txt
    key_end = 0
    #bot.delete_message(message.chat.id, message.message_id)
    number_test = read_line("t", tema)
    it = 0
    test_key = []
    btn_test = []
    keyb_test = types.InlineKeyboardMarkup()

    while it < len(number_test):
        test_key.append("Test" + str(it))
        btn_test.append(types.InlineKeyboardButton(text=number_test[it], callback_data=str(test_key[it])))
        #print(n_t_key[it])
        it += 1

    keyb_test.add(*btn_test)
    #print(btn_test[it])
    #print(tema_testa[i])
    tema_msg=bot.send_message(message.chat.id, tema+" ⬇", reply_markup=keyb_test).message_id
# формирование списка вопросов
def out_quest(n_key):
    global txt
    f = open(txt, "r")
    outline = []
    while True:
        # считываем строку
        line = f.readline()
        # прерываем цикл, если строка пустая
        if not line:
            #print("конец списка")
            break
        if line[0] == "Q" and re.search("_"+n_key+"-\d+\*.*", str(line)):
            readline = "".join(re.findall("_.*\*.*", str(line)))
            #print("".join(re.findall("_(.*)\*.*", str(line))))
            #print(readline)
            outline.append(readline)
    f.close()
    return outline
# формирование списка ответов
def out_answer(n_key):
    global txt
    f = open(txt, "r")
    outline = []
    while True:
        # считываем строку
        line = f.readline()
        # прерываем цикл, если строка пустая
        if not line:
            #print("конец списка")
            break
        if line[0] == "A" and re.search("_"+str(n_key)+"\*.*", str(line)):
            readline = "".join(re.findall("_.*\*(.*)", str(line)))
            #print(readline)
            outline.append(readline)
    f.close()
    return outline
# вывод в бот списка тем
def out_tema(message):
    global no_reg, rez_msg, mes_del, tema_testa, tema_inf, read_key, tema_key, number_test, id_mes_nema , first_msg, msg_vozvrat, txt
    #print(message.text)
    #bot.delete_message(message.chat.id, message.message_id-1)
    if no_reg != 0:
        bot.delete_message(message.chat.id, no_reg)
        no_reg = 0

    if rez_msg != 0:
        bot.delete_message(message.chat.id, rez_msg)
        rez_msg = 0

    if  mes_del == 0:
        mes_del = bot.send_message(message.chat.id, 'Пройдите 📝 ТЕСТ по теме \nили ознакомьтель с материалом 📚 ИНФО ').message_id
        #mes_del = bot.send_message(message.chat.id, 'Пройдите 📝 ТЕСТ по теме \nили ознакомьтель с материалом 📚 ИНФО ',
                                  # reply_markup=None).message_id
    if first_msg != 0:
        bot.delete_message(message.chat.id, first_msg)
        first_msg = 0
    tema_testa = read_line("T",None)
    tema_testa.sort(key=len)
    i = 0
    tema_key = []
    read_key = []
    id_mes_nema = []
    while i < len(tema_testa):
        keyb_tema = types.InlineKeyboardMarkup(row_width=2)
        tema_key.append("Tema"+str(i))
        read_key.append("Read"+str(i))
        btn_read = types.InlineKeyboardButton(text="📚 Инфо ",url='https://yandex.ru/search/?text='+str(tema_testa[i]), callback_data=str(read_key[i]))
        btn_test = types.InlineKeyboardButton(text="📝 Тест ", callback_data=str(tema_key[i]))
        #btn_test = types.InlineKeyboardButton(text="Тучк", callback_data=str(tema_key[i]))

        keyb_tema.add (btn_test, btn_read)
        id_mes_nema.append(bot.send_message(message.chat.id, n_test[i]+"  "+tema_testa[i], reply_markup=keyb_tema).message_id)
        #print(id_mes_nema[i])
        i += 1
    #if first_msg != 0:
    #print("first_msg",first_msg)
    #bot.edit_message_text(message.chat.id, first_msg, "Пыщь")
        #first_msg = 0

    markup = types.ReplyKeyboardMarkup( resize_keyboard=True, )
    item = types.KeyboardButton("Возврат в основное меню")
    markup.add(item)
    msg_vozvrat = bot.send_message(message.chat.id, "вернуться в меню: 👇", reply_markup=markup, ).message_id
    #print("msg_vozvrat", msg_vozvrat)
    #return_keyb(message)
# вывод в бот ответов с вариантами
def out_var(call,i_q,n_q):
    global txt, n_bd, tema, var_otv_msg, vopr_mes,tema_v_vopr,vopr_po_teme, tema_msg, it, answer_key, answer, i_quest, n_t_key , i_tema, num_id, key_end, rezult100, rezult, itog_proc, enddel, enddel1, enddel2, history, final_test

    if tema_msg != 0:
        bot.delete_message(call.message.chat.id, tema_msg)
        tema_msg = 0

    if vopr_po_teme != 0:
        bot.delete_message(call.message.chat.id, vopr_po_teme)
        vopr_po_teme = 0

    if var_otv_msg != 0:
        #print("var_otv_msg",var_otv_msg)
        bot.delete_message(call.message.chat.id, var_otv_msg)
        var_otv_msg = 0
    if vopr_mes != 0:
        #print("vopr_mes",vopr_mes)
        bot.delete_message(call.message.chat.id, vopr_mes)
        vopr_mes = 0

    quest = out_quest(n_q)
    if i_q == len(quest):
        i_q = 0
        #print("Тест завершен")
        key_end = 1
        if rezult == 0:
            inog_proc = 0
        else:
            inog_proc = 100 / (rezult100 / rezult)
        keyb_end = types.InlineKeyboardMarkup(row_width=2)
        enddel=bot.send_message(call.message.chat.id, "✅ Тест закончен - 🏁").message_id
        #print(enddel)
        if round(inog_proc)<50:
            enddel1=bot.send_message(call.message.chat.id, "❌ У вас "+ str(round(inog_proc)) + "% правильных ответов, верных всего " + str(rezult) + " из "+str(rezult100)+ " 👎").message_id
            #print(enddel1)
            history = str("❌ У вас "+ str(round(inog_proc)) + "% правильных ответов, верных всего " + str(rezult) + " из "+str(rezult100)+ " 👎")
        else:
            enddel1=bot.send_message(call.message.chat.id,
                             "✅ У вас "+ str(round(inog_proc)) + "% правильных ответов, верных " + str(rezult) + " из "+str(rezult100)+ " 👍").message_id
            #print(enddel1)
            history = str("✅ У вас "+ str(round(inog_proc)) + "% правильных ответов, верных " + str(rezult) + " из "+str(rezult100)+ " 👍")
        write_rez(history, n_bd)
        btn_end1=types.InlineKeyboardButton(text="Завершить", callback_data="завершить")
        btn_end2=types.InlineKeyboardButton(text='Выбрать другой тест', callback_data="выбрать")
        keyb_end.row(btn_end1,btn_end2)
        enddel2=bot.send_message(call.message.chat.id, text="👇 Выберите дальнейшие действия", reply_markup=keyb_end).message_id
        #print(enddel2)

    if key_end == 0:
        n_quest = "".join(re.findall("_.*\*(.*)", quest[i_q]))
        n_answ = "".join(re.findall("_(.*)\*.*", quest[i_q]))
        answer = out_answer(n_answ)
        iA = 0
        keyb_answer = types.InlineKeyboardMarkup(row_width=len(answer))
        vopr_mes = bot.send_message(call.message.chat.id, "🟡 "+str(tema)+"\nВопрос № "+str(i_q+1)+ " из "+ str(len(quest)) ).message_id
        text_q = "🟢 "+str(n_quest.replace('/n', '\n'))+"\n"
        answer_key = []
        btn_answer = []
        while iA < len(answer):
            # print(answer[iA])
            answer_key.append("answ"+str(iA))
            btn_answer.append(types.InlineKeyboardButton(text='Вариант '+ str(iA+1) , callback_data=answer_key[iA]))
            text_q = text_q+answer[iA][:-1]+"\n"
            iA += 1
        keyb_answer.row(*btn_answer)
        var_otv_msg=bot.send_message(call.message.chat.id, text_q, reply_markup=keyb_answer).message_id
#Запись результата в БД
def write_rez(hist,call_u_name):

    try:

        query1 = "UPDATE test SET result = '" + hist + "' WHERE username = '"+call_u_name+"' "
        database = 'database.db'
        connection = sqlite3.connect(database)
        #print("Подключен к SQLite")
        connection.execute(query1)
        connection.commit()
        connection.close()
        #print("Результат успешно добавлен")
        connection.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            #print("Соединение с SQLite закрыто")
# чтение значений sql
def read_rez(call_u_name,noreg):
    out_rez='0'
    #print(out_rez,call_u_name,noreg )
    if noreg == "1": # проверка наличия юзера в базе
        try:
            con = sqlite3.connect('database.db')
            cursorObj = con.cursor()
            cursorObj.execute("SELECT username FROM test WHERE username ='" + call_u_name + "'")
            rows = cursorObj.fetchall()
            for row in rows:
                out_rez = "1"
                #print(out_rez)
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if con:
                con.close()
                #print("Соединение с SQLite закрыто 1")
        #print("regist", out_rez)

    elif noreg == "2": # получение результатов теста
        try:
            con = sqlite3.connect('database.db')
            cursorObj = con.cursor()
            cursorObj.execute("SELECT result FROM test WHERE username ='" + call_u_name + "'")
            rows = cursorObj.fetchall()
            for row in rows:
                out_rez = str(row)
                out_rez = out_rez[2:len(out_rez) - 3]
                #print(out_rez)

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if con:
                con.close()
                #print("Соединение с SQLite закрыто 2")
        #print("rez",out_rez)
    elif noreg == "3": # получение отдела
        try:
            con = sqlite3.connect('database.db')
            cursorObj = con.cursor()
            cursorObj.execute("SELECT service FROM test WHERE username ='" + call_u_name + "'")
            rows = cursorObj.fetchall()
            for row in rows:
                out_rez = str(row)
                out_rez = out_rez[2:len(out_rez) - 3]
                #print(out_rez)

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if con:
                con.close()
                #print("Соединение с SQLite закрыто 2")
        #print("rez",out_rez)

    return(out_rez)

#База данных
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, service: str, tab_number: str, result: str):
    cursor.execute('INSERT INTO test(user_id, user_name, user_surname, username, service, tab_number, result) VALUES (?,?,?,?,?,?,?)',
                   (user_id, user_name, user_surname, username, service, tab_number, result))
    conn.commit()
# обработка start end
@bot.message_handler(commands=['start','end'])
def send_welcome(message):
    global first_msg,noreg_msg,n_bd, re_reg, by_msg,txt
    if message.text == "/end":
        by_msg = bot.send_message(message.chat.id,\
                                     "👋 До встречи...").message_id
        bot.delete_message(message.chat.id, message.message_id)

    if message.text == "/start":
        #bot.delete_message(message.chat.id, message.message_id)
        #print (message.from_user.username)
        if message.from_user.username == None: # если не задан username то username=user_id
            #print('нет Юзернэйма')
            n_bd = str(message.from_user.id)
        else:
            n_bd = message.from_user.username


        if read_rez(n_bd, "3") == "0" or read_rez(n_bd, "3") == '':
            txt = "bd.txt"
            #print("по умолчанию",txt)
        else:
            # выбор варианта теста на основе указанного отдела
            ser = read_rez(n_bd, "3")
            #print(ser)
            pat1 = re.compile(
                r'(?i)(.*кад.*|.*бух.*|.*арх.*)')  # упращенная тематика теста не IT направленность отделов
            pat2 = re.compile(r'(?i)(.*ит.*|.*it.*|.*киб.*)')  # тесты для отделов IT направленности
            if re.search(pat2, ser):

                txt = "bd2.txt"
                #print(txt)
            elif re.search(pat1, ser):

                txt = "bd1.txt"
                #print(txt)
            else:

                txt = "bd.txt"
                #print(txt)

        #print(n_bd)

        if by_msg != 0:
            bot.delete_message(message.chat.id, by_msg)
            by_msg = 0
        if re_reg != 0:
            bot.delete_message(message.chat.id, re_reg)
            re_reg = 0
        if noreg_msg != 0:
            bot.delete_message(message.chat.id, noreg_msg)
            noreg_msg = 0
        #bot.delete_message(message.chat.id, message.message_id)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #, one_time_keyboard=True)
    item1 = types.KeyboardButton("Регистрация")
    item2 = types.KeyboardButton("Выбор темы")
    item3 = types.KeyboardButton("Результат")
    markup.add(item1, item2, item3)
    if first_msg == 0:

        first_msg = bot.send_message(message.chat.id, "Вас приветствует чат-бот тестирования по вопросам ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ🛡\nСледуя подсказкам бота, выбирайте дальнешие действия кнопками меню 👇", reply_markup=markup).message_id
    elif first_msg != 0:
        bot.delete_message(message.chat.id, first_msg)
        first_msg = bot.send_message(message.chat.id,\
                                     "Вас приветствует чат-бот тестирования по вопросам ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ🛡\nСледуя подсказкам бота, выбирайте дальнешие действия кнопками меню 👇",\
                                     reply_markup=markup).message_id

    #print(first_msg)
# обработка кнопок меню и текстовых сообщений от пользователя
@bot.message_handler(content_types=['text'])
def choice(message):
    global  by_msg, re_reg, noreg_msg, n_bd , no_reg, rez_msg, test, tema_testa, tema_inf, read_key, test_key, n_t_key, btn, answer, number_test, mes_del, history, new_test, id_mes_nema, ferst_msg, msg_vozvrat, key_reg
    if message.text not in 'Возврат в основное меню Регистрация Результат Выбор темы /end':
        #print("NO")
        bot.delete_message(message.chat.id, message.message_id)
    else:
        print(" ")

    if message.text == "Возврат в основное меню":
        if noreg_msg != 0:
            bot.delete_message(message.chat.id, noreg_msg)
            noreg_msg = 0
        bot.delete_message(message.chat.id, message.message_id)
        if no_reg != 0:
            bot.delete_message(message.chat.id, no_reg)
            no_reg = 0

        if msg_vozvrat != 0:
            bot.delete_message(message.chat.id, msg_vozvrat)
            msg_vozvrat = 0
        if mes_del != 0:
            bot.delete_message(message.chat.id, mes_del)
            mes_del = 0
        i = 0
        #print(id_mes_nema)
        if id_mes_nema != '':
            while i < len(id_mes_nema):
                bot.delete_message(message.chat.id, id_mes_nema[i])
                i += 1
        send_welcome(message)

    if message.text == 'Регистрация':
        if by_msg != 0:
            bot.delete_message(message.chat.id, by_msg)
            by_msg = 0
        if re_reg != 0:
            bot.delete_message(message.chat.id, re_reg)
            re_reg = 0
        if noreg_msg != 0:
            bot.delete_message(message.chat.id, noreg_msg)
            noreg_msg = 0
        if rez_msg != 0:
            bot.delete_message(message.chat.id, rez_msg)
            rez_msg = 0
        if no_reg != 0:
            bot.delete_message(message.chat.id, no_reg)
            no_reg = 0
        bot.delete_message(message.chat.id, message.message_id)
        if read_rez(n_bd, "1") == '1':
            re_reg = bot.send_message(message.chat.id,
                                      "⚠ Вы уже зарегистрированы, для корректировки сведений обратитетсь к администратору бота").message_id
        else:
            bot.send_message(message.chat.id,'Введите Ваше имя?',reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, rt_name)

    if message.text == "Результат":
        bot.delete_message(message.chat.id, message.message_id)
        if by_msg != 0:
            bot.delete_message(message.chat.id, by_msg)
            by_msg = 0
        if re_reg != 0:
            bot.delete_message(message.chat.id, re_reg)
            re_reg = 0
        if noreg_msg != 0:
            bot.delete_message(message.chat.id, noreg_msg)
            noreg_msg = 0

        if no_reg != 0:
            bot.delete_message(message.chat.id, no_reg)
            no_reg = 0
        if rez_msg != 0:
            bot.delete_message(message.chat.id, rez_msg)
            rez_msg = 0
        if read_rez(n_bd,"2") == "0" or read_rez(n_bd,"2") == '' :
            rez_msg = bot.send_message(message.chat.id, "Нет пройденных тестов").message_id
        else :
            rez_msg=bot.send_message(message.chat.id,read_rez(n_bd,"2")).message_id

    if message.text == "Выбор темы":
        bot.delete_message(message.chat.id, message.message_id)
        if by_msg != 0:
            bot.delete_message(message.chat.id, by_msg)
            by_msg = 0
        if re_reg != 0:
            bot.delete_message(message.chat.id, re_reg)
            re_reg = 0
        if rez_msg != 0:
            bot.delete_message(message.chat.id, rez_msg)
            rez_msg = 0
        if noreg_msg != 0:
            bot.delete_message(message.chat.id, noreg_msg)
            noreg_msg = 0
        if read_rez(n_bd,"1") == '1':

            mes_del = bot.send_message(message.chat.id, 'Пройдите 📝 ТЕСТ по теме \nили ознакомьтель с материалом 📚 ИНФО ',reply_markup=None).message_id
            if rez_msg != 0:
                bot.delete_message(message.chat.id, rez_msg)
                rez_msg = 0
            all_sbros()
            #print(mes_del)
            out_tema(message)
        else:
            noreg_msg = bot.send_message(message.chat.id, "⚠ Для прохождения теста требуется зарегистрироваться.\nВоспользуйтесь соответствующим пунктом меню").message_id
#ПЕРЕХОД К ФАМИЛИИ
def rt_name(message):
    global name_bd, no_reg,key_reg
    if no_reg != 0:
        bot.delete_message(message.chat.id, no_reg)
        no_reg = 0
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
    name_bd = message.text
    bot.send_message(message.chat.id, 'Уточните вашу фамилию:')
    bot.register_next_step_handler(message, rt_surname)
#ПЕРЕХОД К ОТДЕЛУ
def rt_surname(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    global surname
    surname = message.text
    bot.send_message(message.chat.id, 'Укажите отдел/подразделение в котором вы работаете?\n("отдел кадров", "бухгалтерия", "служба безопасности" и пр.')
    bot.register_next_step_handler(message, rt_service)
#ТАБЕЛЬНЫЙ НОМЕР
def rt_service(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    global service, txt
    service = message.text
    # выбор варианта теста на основе указанного отдела
    pat1 = re.compile(r'(?i)(.*кад.*|.*бух.*|.*арх.*)')  # упращенная тематика теста не IT направленность отделов
    pat2 = re.compile(r'(?i)(.*ит.*|.*it.*|.*киб.*)')  # тесты для отделов IT направленности
    if re.search(pat2, service):
        #print("тест 1")
        txt = "bd2.txt"
    elif re.search(pat1, service):
        #print("тест 2")
        txt = "bd1.txt"
    else:
        #print("тест 4")
        txt = "bd.txt"

    bot.send_message(message.chat.id, 'Ваш табельный номер?')
    bot.register_next_step_handler(message, rt_tabn)
# кнопки подтверждения регистрации
def rt_tabn(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    global tabn
    tabn = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='✅ Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='❎ Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Давайте проверим.\nВас зовут ' + name_bd + '  ' +  surname + ',' + ' вы работаете в службе ' + service + ', ' + 'ваш табельный номер ' + tabn + ', все верно ?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
# обработка подтверждения корректности регистрации
@bot.callback_query_handler(lambda call: call.data == "yes" or call.data == "no")
def reg(call):
    global no_reg, key_reg, msg_vozvrat, n_bd
    if call.data == "yes":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        people_id = call.message.chat.id
        cursor.execute(f"SELECT user_id FROM test WHERE user_id = {people_id}")
        data = cursor.fetchone()
        if data is None:
            key_reg = 1
            no_reg = bot.send_message(call.message.chat.id, 'Вы добавлены!').message_id
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
            item = types.KeyboardButton("Возврат в основное меню")
            markup.add(item)
            msg_vozvrat = bot.send_message(call.message.chat.id, "вернуться в меню: 👇", reply_markup=markup, ).message_id
            us_id = call.from_user.id
            us_name = name_bd
            us_sname = surname
            username = n_bd
            ser = service
            tab_number = tabn
            rez = ''
            db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname,
                         username=username, service=ser, tab_number=tab_number, result=rez)
        else:
            key_reg = 1
            no_reg = bot.send_message(call.message.chat.id, "Вы уже зарегистрированы, для корректировки сведений обратитетсь к администратору бота").message_id
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
            item = types.KeyboardButton("Возврат в основное меню")
            markup.add(item)
            msg_vozvrat = bot.send_message(call.message.chat.id, "вернуться в меню: 👇", reply_markup=markup, ).message_id

    elif call.data == "no":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        no_reg = bot.send_message(call.message.chat.id, 'Давайте попробуем еще раз.\nНазавите Ваше Имя:').message_id
        bot.register_next_step_handler(call.message, rt_name)
# обработка всех кнопок теста
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global tema_v_vopr, vopr_po_teme, test, tema_testa, tema_inf, read_key, tema_key, tema, test_key, n_t_key , n_answ, iQ, it, answer_key, answer, i_quest , i_tema, rezult, rezult100, mes_del, enddel, enddel1,enddel2, msg_vozvrat, new_test, id_mes_nema, first_msg

    if call.data == "завершить":
        if enddel != 0:
            bot.delete_message(call.message.chat.id, enddel)
            enddel = 0
        if enddel1 != 0:
            bot.delete_message(call.message.chat.id, enddel1)
            enddel1 = 0
        if enddel2 != 0:
            bot.delete_message(call.message.chat.id, enddel2)
            enddel2 = 0
        send_welcome(call.message)

    if call.data == "выбрать":
        all_sbros()
        if enddel != 0:
            bot.delete_message(call.message.chat.id, enddel)
            enddel = 0
        if enddel1 != 0:
            bot.delete_message(call.message.chat.id, enddel1)
            enddel1 = 0
        if enddel2 != 0:
            bot.delete_message(call.message.chat.id, enddel2)
            enddel2 = 0
        out_tema(call.message)

    i = 0
    iA = 0
    if answer != '':
        while iA < len(answer):
            if call.data == answer_key[iA]:
                if answer[iA][-1] == "-":
                    rezult -= 1
                i_quest += 1
                out_var(call,i_quest,i_tema)
            iA += 1

    if number_test != '':
        while  it < len(number_test):
            if call.data == test_key[it]:
                i_tema = n_t_key[it]
                i_quest = 0
                rezult100 = len(out_quest(i_tema))
                #print("всего", rezult100)
                rezult = rezult100
                #print("100% это",rezult,"верных ответов")
                out_var(call,i_quest,i_tema)
            it += 1

        while i < len(tema_testa):

            if call.data == tema_key[i]:
                if msg_vozvrat != 0:
                    bot.delete_message(call.message.chat.id, msg_vozvrat)
                    msg_vozvrat = 0
                if mes_del != 0:
                    bot.delete_message(call.message.chat.id, mes_del)
                    mes_del = 0
                ii = 0
                #print(id_mes_nema)
                while ii < len(id_mes_nema):
                    bot.delete_message(call.message.chat.id, id_mes_nema[ii])
                    ii += 1
                tema = tema_testa[i]
                test_key = []
                vopr_po_teme=bot.send_message(call.message.chat.id, text="Вопросы по теме 👇:", reply_markup=None).message_id
                out_test(call.message)
            i+=1
    return

#create_test() #парсинг тестов с сайта
#file_r_w() #подготовка bd файла с перечнем материала
bot.polling()
