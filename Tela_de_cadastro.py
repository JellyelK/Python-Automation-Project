from guizero import App, Text, TextBox, PushButton, Window

def confirm_login():
    # janela = Window(app, title="Cliente cadastrado com sucesso", width=300, height=200)
    # text_confirm = Text(janela, text="Cliente cadastrado com sucesso!")
    global cliente
    global senha
    cliente.clear()
    senha.clear()
    # btn_confirm = PushButton(janela, text='Avançar', command=janela.destroy)



#Interface da aplicação

app = App(title='Tela de cadastro', layout="grid", width=320,  height=300)

txt_cliente = Text(app, text='Cliente: ', grid=[0, 0])
cliente = TextBox(app, grid=[1, 0], width=30)

txt_senha = Text(app, text='Senha: ', grid=[0, 2])
senha = TextBox(app, hide_text=True, grid=[1, 2], width=30)

btn_cadastrar = PushButton(app, text='Cadastrar', command=confirm_login, grid=[1, 4], width=20)
app.display()