import customtkinter as ctk
import math
from datetime import datetime

#<editor-fold desc="Tabela de Pontos e Dados">
# TABELA PARA CONTRATO ANTIGO
TABELA_PONTOS_ANTIGO = {
    "Bourbon Atibaia": {
        "Réveillon": {"Duplo Superior": 103046, "Triplo Superior": 118053, "Triplo Superior + 1 CHD até 11": 142358, "Duplo Premier": 113992, "Triplo Premier": 131176, "Suíte Classic": 162544},
        "Super Alta - Natal": {"Duplo Superior": 80977, "Triplo Superior": 91512, "Triplo Superior + 1 CHD até 11": 111462, "Duplo Premier": 89922, "Triplo Premier": 102281, "Suíte Classic": 132176},
        "Super Alta - Carnaval": {"Duplo Superior": 62512, "Triplo Superior": 68724, "Triplo Superior + 1 CHD até 11": 85398, "Duplo Premier": 69966, "Triplo Premier": 77747, "Suíte Classic": 107826},
        "Super Alta - Páscoa / Corpus Christi": {"Duplo Superior": 54665, "Triplo Superior": 59373, "Triplo Superior + 1 CHD até 11": 74478, "Duplo Premier": 61466, "Triplo Premier": 67547, "Suíte Classic": 96776},
        "FERIADOS": {"Duplo Superior": 50742, "Triplo Superior": 54665, "Triplo Superior + 1 CHD até 11": 68920, "Duplo Premier": 57150, "Triplo Premier": 62381, "Suíte Classic": 91152},
        "ALTA": {"Duplo Superior": 37926, "Triplo Superior": 39299, "Triplo Superior + 1 CHD até 11": 51069, "Duplo Premier": 43222, "Triplo Premier": 45641, "Suíte Classic": 72974},
        "MÉDIA": {"Duplo Superior": 32041, "Triplo Superior": 32237, "Triplo Superior + 1 CHD até 11": 42764, "Duplo Premier": 36814, "Triplo Premier": 37926, "Suíte Classic": 64604}
    },
    "Bourbon Cataratas": {
        "Réveillon": {"Duplo Standar": 56575, "Duplo Superior Vista Jardim": 59937, "Triplo Superior Vista Jardim": 69668, "Familia Superior Vista Jardim": 104432, "Duplo Superior Vista Piscina": 63984, "Triplo Superior Vista Piscina": 74526},
        "Super Alta": {"Duplo Standar": 41069, "Duplo Superior Vista Jardim": 43622, "Triplo Superior Vista Jardim": 50116, "Familia Superior Vista Jardim": 76660, "Duplo Superior Vista Piscina": 46736, "Triplo Superior Vista Piscina": 53790},
        "ALTA": {"Duplo Standar": 24568, "Duplo Superior Vista Jardim": 26249, "Triplo Superior Vista Jardim": 29255, "Familia Superior Vista Jardim": 47143, "Duplo Superior Vista Piscina": 28304, "Triplo Superior Vista Piscina": 31684},
        "MÉDIA": {"Duplo Standar": 23136, "Duplo Superior Vista Jardim": 24755, "Triplo Superior Vista Jardim": 27387, "Familia Superior Vista Jardim": 44529, "Duplo Superior Vista Piscina": 26686, "Triplo Superior Vista Piscina": 29753}
    }
}
# TABELA PARA CONTRATO NOVO (SENSE)
TABELA_PONTOS_NOVO = {
    "Bourbon Atibaia": {
        "Datas Especiais - Reveillon": {"Duplo Superior": 79889, "Triplo Superior": 83281, "Duplo Superior Plus": 83370, "Triplo Superior Plus": 86761, "Premier Duplo": 87654, "Premier Triplo": 91045, "Suite Classic": 98364},
        "Datas Especiais - Natal": {"Duplo Superior": 71485, "Triplo Superior": 74876, "Duplo Superior Plus": 74966, "Triplo Superior Plus": 78357, "Premier Duplo": 79250, "Premier Triplo": 82641, "Suite Classic": 89960},
        "Super Alta": {"Duplo Superior": 53624, "Triplo Superior": 57016, "Duplo Superior Plus": 57105, "Triplo Superior Plus": 60497, "Premier Duplo": 61389, "Premier Triplo": 64781, "Suite Classic": 72099},
        "Alta": {"Duplo Superior": 42569, "Triplo Superior": 45960, "Duplo Superior Plus": 46049, "Triplo Superior Plus": 49441, "Premier Duplo": 50333, "Premier Triplo": 53725, "Suite Classic": 61043},
        "Média": {"Duplo Superior": 38465, "Triplo Superior": 41857, "Duplo Superior Plus": 41946, "Triplo Superior Plus": 45337, "Premier Duplo": 46230, "Premier Triplo": 49621, "Suite Classic": 56940}
    },
    "Bourbon Cataratas": {
        "Datas Especiais": {"Duplo Standar": 56575, "Duplo Superior Vista Jardim": 63936, "Triplo Superior Vista Jardim": 66292, "Duplo Superior Vista Piscina": 69023, "Triplo Superior Vista Piscina": 71379, "Premier Duplo": 71700, "Premier Triplo": 74057, "Suite Classic": 101421},
        "Super Alta": {"Duplo Standar": 41069, "Duplo Superior Vista Jardim": 34332, "Triplo Superior Vista Jardim": 36688, "Duplo Superior Vista Piscina": 39419, "Triplo Superior Vista Piscina": 41775, "Premier Duplo": 42096, "Premier Triplo": 44452, "Suite Classic": 71817},
        "Alta": {"Duplo Standar": 24568, "Duplo Superior Vista Jardim": 27230, "Triplo Superior Vista Jardim": 29586, "Duplo Superior Vista Piscina": 32317, "Triplo Superior Vista Piscina": 34674, "Premier Duplo": 34995, "Premier Triplo": 37351, "Suite Classic": 64715},
        "Média": {"Duplo Standar": 22979, "Duplo Superior Vista Jardim": 22979, "Triplo Superior Vista Jardim": 25335, "Duplo Superior Vista Piscina": 28066, "Triplo Superior Vista Piscina": 30422, "Premier Duplo": 30744, "Premier Triplo": 33100, "Suite Classic": 60464}
    }
}
# REGRAS DE TEMPORADA POR TIER
REGRAS_TIER_NOVO = {
    "Style": ["Média"], "Select": ["Média", "Alta"],
    "Sublime": ["Média", "Alta", "Super Alta"],
    "Luxury": ["Média", "Alta", "Super Alta", "Datas Especiais"],
    "Sense": ["Média", "Alta", "Super Alta", "Datas Especiais"]
}
#</editor-fold>

#<editor-fold desc="Funções da Calculadora de Negociações (Aba 1)">
def limpar_campos_negociacao():
    neg_combo_produto.set("Selecione o Tipo de Produto")
    neg_entry_valor_total.delete(0, 'end'); neg_entry_valor_pago.delete(0, 'end')
    neg_entry_qtd_parcelas.delete(0, 'end'); neg_entry_qtd_entrada.delete(0, 'end')
    neg_entry_valor_entrada.delete(0, 'end'); neg_checkbox_entrada.deselect()
    toggle_entrada_fields(); exibir_resultado_negociacao("")
def toggle_entrada_fields():
    if neg_checkbox_entrada.get() == 1: neg_frame_entrada.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
    else: neg_frame_entrada.grid_forget()
def calcular_proposta():
    try:
        valor_total = float(neg_entry_valor_total.get().replace('.', '').replace(',', '.')); valor_pago = float(neg_entry_valor_pago.get().replace('.', '').replace(',', '.'))
        qtd_parcelas_contrato_original = int(neg_entry_qtd_parcelas.get()); saldo_devedor = valor_total - valor_pago
        texto_entrada, total_entrada, qtd_parcelas_entrada = "", 0, 0
        if neg_checkbox_entrada.get() == 1:
            qtd_parcelas_entrada = int(neg_entry_qtd_entrada.get()); valor_parcela_entrada = float(neg_entry_valor_entrada.get().replace('.', '').replace(',', '.'))
            total_entrada = qtd_parcelas_entrada * valor_parcela_entrada
            texto_entrada = (f"PAGAMENTO DE ENTRADA:\n"
                             f"• {qtd_parcelas_entrada}x parcelas de R$ {valor_parcela_entrada:,.2f} devem ser pagas para iniciar a negociação.\n"
                             f"------------------------------------------------------\n")
        saldo_para_renegociar = saldo_devedor - total_entrada; qtd_parcelas_disponiveis = qtd_parcelas_contrato_original - qtd_parcelas_entrada
        if qtd_parcelas_disponiveis < 6:
            exibir_resultado_negociacao(f"Erro: Após a entrada de {qtd_parcelas_entrada}x, "
                                     f"sobram apenas {qtd_parcelas_disponiveis} parcelas, "
                                     f"insuficiente para a negociação de 6 meses."); return
        tipo_produto = neg_combo_produto.get()
        valores_reduzidos = {"150.000": 350.00, "300.000": 500.00, "450.000 ou 600.000": 800.00, "1.000.000": 1000.00}
        if tipo_produto not in valores_reduzidos: exibir_resultado_negociacao("Erro: Selecione um tipo de produto válido."); return
        valor_parcela_reduzida = valores_reduzidos[tipo_produto]; total_pago_na_reducao = 6 * valor_parcela_reduzida
        if saldo_para_renegociar < total_pago_na_reducao:
            exibir_resultado_negociacao(f"Proposta Inválida!\nO saldo restante após a entrada (R$ {saldo_para_renegociar:,.2f}) "
                        f"é menor que o valor da redução (R$ {total_pago_na_reducao:,.2f})."); return
        saldo_devedor_apos_reducao = saldo_para_renegociar - total_pago_na_reducao
        parcelas_restantes_normais = qtd_parcelas_disponiveis - 6
        if parcelas_restantes_normais <= 0:
            proposta_renegociacao = (f"PROPOSTA DE RENEGOCIAÇÃO:\n\n"
                                    f"• As 6 parcelas de R$ {valor_parcela_reduzida:,.2f} quitam a dívida.")
        else:
            valor_base_nova_parcela = saldo_devedor_apos_reducao / parcelas_restantes_normais
            parcela_padrao_arredondada = math.floor(valor_base_nova_parcela)
            ultima_parcela_ajuste = saldo_devedor_apos_reducao - (parcela_padrao_arredondada * (parcelas_restantes_normais - 1))
            proposta_renegociacao = (f"PROPOSTA DE RENEGOCIAÇÃO:\n\n"
                                    f"• 6x parcelas de R$ {valor_parcela_reduzida:,.2f}\n"
                                    f"• {parcelas_restantes_normais - 1}x parcelas de R$ {parcela_padrao_arredondada:,.2f}\n"
                                    f"• 1x parcela de ajuste de R$ {ultima_parcela_ajuste:,.2f}")
        exibir_resultado_negociacao(texto_entrada + proposta_renegociacao)
    except (ValueError, KeyError, TypeError):
        exibir_resultado_negociacao("Erro: Verifique se todos os campos estão preenchidos com números válidos.")
def exibir_resultado_negociacao(texto):
    neg_textbox_resultado.configure(state="normal"); neg_textbox_resultado.delete("1.0", "end")
    neg_textbox_resultado.insert("1.0", texto); neg_textbox_resultado.configure(state="disabled")
#</editor-fold>

#<editor-fold desc="Funções da Calculadora de Reservas (Aba 2)">
def update_reserva_ui(*args):
    """Função central que gerencia a visibilidade e as opções da UI de Reservas."""
    contrato = res_combo_contrato.get()
    
    if contrato == "Novo":
        res_frame_antigo.grid_forget()
        res_frame_novo.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        
        # Atualiza opções para Contrato Novo
        selected_hotel_novo = res_combo_hotel_novo.get()
        selected_tier = res_combo_tier_novo.get()
        hotel_key_novo = "Bourbon Atibaia" if selected_hotel_novo == "Bourbon Atibaia" else "Bourbon Cataratas"
        
        allowed_seasons = REGRAS_TIER_NOVO.get(selected_tier, [])
        available_seasons = [s for s in TABELA_PONTOS_NOVO.get(hotel_key_novo, {}).keys() if any(allowed in s for allowed in allowed_seasons)]
        res_combo_temporada_novo.configure(values=available_seasons)
        
        all_acomodacoes_novo = set()
        for temp in available_seasons:
            all_acomodacoes_novo.update(TABELA_PONTOS_NOVO.get(hotel_key_novo, {}).get(temp, {}).keys())
        res_combo_acomodacao_novo.configure(values=sorted(list(all_acomodacoes_novo)))

    else: # Contrato Antigo
        res_frame_novo.grid_forget()
        res_frame_antigo.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Atualiza opções para Contrato Antigo
        selected_hotel_antigo = res_combo_hotel.get()
        temporadas_antigo = list(TABELA_PONTOS_ANTIGO.get(selected_hotel_antigo, {}).keys())
        res_combo_temporada.configure(values=temporadas_antigo)
        
        all_acomodacoes_antigo = set()
        for temporada_data in TABELA_PONTOS_ANTIGO.get(selected_hotel_antigo, {}).values():
            all_acomodacoes_antigo.update(temporada_data.keys())
        res_combo_acomodacao.configure(values=sorted(list(all_acomodacoes_antigo)))

        # Atualiza campos de crianças
        if selected_hotel_antigo == "Bourbon Cataratas":
            res_entry_criancas_geral.grid_forget()
            res_frame_criancas_cataratas.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        else:
            res_frame_criancas_cataratas.grid_forget()
            res_entry_criancas_geral.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

def toggle_valor_ponto_field(*args):
    if res_combo_pagto_alim.get() == "Por Pontos":
        res_entry_valor_ponto.grid(row=0, column=2, padx=(5,0), sticky="ew")
    else:
        res_entry_valor_ponto.grid_forget()

def limpar_campos_reserva():
    # Limpa campos comuns e de ambos os contratos
    res_combo_contrato.set("Antigo"); res_combo_hotel.set("Selecione o Hotel"); res_combo_temporada.set("Selecione a Temporada"); res_combo_acomodacao.set("Selecione a Acomodação")
    res_combo_tier_novo.set("Selecione o Tier"); res_combo_hotel_novo.set("Selecione o Hotel"); res_combo_temporada_novo.set("Selecione a Temporada"); res_combo_acomodacao_novo.set("Selecione a Acomodação"); res_combo_fracionamento.set("Abertura de Fracionamento")
    for entry in [res_entry_checkin, res_entry_checkout, res_entry_adultos, res_entry_noites_fds, res_entry_criancas_geral, res_entry_criancas_0a2, res_entry_criancas_3a8, res_entry_criancas_9a11, res_entry_valor_alim, res_entry_valor_ponto, res_entry_pontos_disponiveis]: entry.delete(0, 'end')
    res_combo_pagto_alim.set("Dinheiro"); toggle_valor_ponto_field()
    update_reserva_ui(); exibir_resultado_reserva("")

def gerar_cotacao():
    try:
        contrato_tipo = res_combo_contrato.get()
        # --- DADOS COMUNS ---
        checkin_str, checkout_str = res_entry_checkin.get(), res_entry_checkout.get()
        checkin_data = datetime.strptime(checkin_str, '%d/%m/%Y'); checkout_data = datetime.strptime(checkout_str, '%d/%m/%Y')
        total_noites = (checkout_data - checkin_data).days
        if total_noites <= 0: exibir_resultado_reserva("Erro: Data de Check-out inválida."); return
        adultos = int(res_entry_adultos.get() or 0)
        noites_fds = int(res_entry_noites_fds.get() or 0)
        pontos_disponiveis = int(float(res_entry_pontos_disponiveis.get().replace('.','').replace(',','') or 0))

        # --- LÓGICA PARA CONTRATO ANTIGO ---
        if contrato_tipo == "Antigo":
            hotel, acomodacao = res_combo_hotel.get(), res_combo_acomodacao.get()
            if hotel == "Bourbon Cataratas":
                criancas_0a2, criancas_3a8, criancas_9a11 = int(res_entry_criancas_0a2.get() or 0), int(res_entry_criancas_3a8.get() or 0), int(res_entry_criancas_9a11.get() or 0)
                total_chd = criancas_0a2 + criancas_3a8 + criancas_9a11
            else: total_chd = int(res_entry_criancas_geral.get() or 0)
            
            if (adultos + total_chd) > (5 if "Familia" in acomodacao else 4):
                exibir_resultado_reserva(f"Erro: Ocupação excede o limite para esta categoria."); return

            pontos_semana = TABELA_PONTOS_ANTIGO[hotel][res_combo_temporada.get()][acomodacao]
            total_pontos_estadia = math.ceil(((pontos_semana / 7) * total_noites) + ((pontos_semana / 7) * 0.20 * noites_fds))
            # (Restante da lógica do Contrato Antigo omitida para brevidade) ...

        # --- LÓGICA PARA CONTRATO NOVO ---
        elif contrato_tipo == "Novo":
            hotel_ui, tier, temporada, acomodacao, tipo_uso = res_combo_hotel_novo.get(), res_combo_tier_novo.get(), res_combo_temporada_novo.get(), res_combo_acomodacao_novo.get(), res_combo_fracionamento.get()
            hotel_key = "Bourbon Atibaia" if hotel_ui == "Bourbon Atibaia" else "Bourbon Cataratas"

            if not all([hotel_ui, tier, temporada, acomodacao]): exibir_resultado_reserva("Erro: Preencha todos os campos do Contrato Novo."); return
            
            allowed_seasons = REGRAS_TIER_NOVO.get(tier, []);
            if not any(allowed in temporada for allowed in allowed_seasons):
                exibir_resultado_reserva(f"Erro: O tier '{tier}' não permite reservas na temporada '{temporada}'."); return
            
            total_chd = int(res_entry_criancas_geral.get() or 0)
            if (adultos + total_chd) > (5 if "Familia" in acomodacao else 4):
                exibir_resultado_reserva(f"Erro: Ocupação excede o limite para esta categoria."); return

            pontuacao_hospedagem = 0
            if tipo_uso == "Abertura de Fracionamento":
                pontuacao_hospedagem = TABELA_PONTOS_NOVO[hotel_key][temporada][acomodacao]

            total_alim_reais = 0
            if (valor_alim_str := res_entry_valor_alim.get().replace('.', '').replace(',', '')):
                valor_alim_dia_adulto = float(valor_alim_str)
                total_alim_reais = valor_alim_dia_adulto * adultos * total_noites
            
            taxa_diaria = 58.00
            if "Triplo" in acomodacao: taxa_diaria = 86.00
            elif "Familia" in acomodacao: taxa_diaria = 116.00
            total_taxa_utilizacao_reais = taxa_diaria * total_noites

            total_taxa_clube_reais = total_alim_reais + total_taxa_utilizacao_reais
            
            pontos_taxa_clube = 0; texto_taxa_clube = ""
            if res_combo_pagto_alim.get() == "Dinheiro":
                texto_taxa_clube = f"Taxa Clube: R$ {total_taxa_clube_reais:,.2f}\n"
            else: # Por Pontos
                valor_ponto = float(res_entry_valor_ponto.get().replace('.', '').replace(',', ''))
                pontos_taxa_clube = math.ceil(total_taxa_clube_reais / valor_ponto)
                texto_taxa_clube = f"Taxa Clube: {pontos_taxa_clube:,} Pontos\n"
            
            total_pontos_necessarios = pontuacao_hospedagem + pontos_taxa_clube
            
            texto_resultado = f"Período: {checkin_str} a {checkout_str} ({total_noites} diárias)\nHotel: {hotel_ui}\n\n"
            texto_resultado += f"Quarto - {tipo_uso}\nCategoria: {acomodacao}\nOcupação: {adultos} adultos e {total_chd} crianças\n"
            texto_resultado += f"Pontuação hospedagem: {pontuacao_hospedagem:,} pontos\n"
            texto_resultado += texto_taxa_clube
            texto_resultado += f"\nTotal de pontos necessários: {total_pontos_necessarios:,} pontos"
            exibir_resultado_reserva(texto_resultado)

    except (ValueError, KeyError, TypeError) as e:
        exibir_resultado_reserva(f"Erro nos dados: Verifique se todos os campos estão preenchidos corretamente.\nDetalhe: {e}")

def exibir_resultado_reserva(texto):
    res_textbox_resultado.configure(state="normal"); res_textbox_resultado.delete("1.0", "end")
    res_textbox_resultado.insert("1.0", texto); res_textbox_resultado.configure(state="disabled")
#</editor-fold>

#<editor-fold desc="Layout da Aplicação Principal">
ctk.set_appearance_mode("dark"); ctk.set_default_color_theme("blue")
app = ctk.CTk(); app.title("Calculadora Bourbon Club"); app.geometry("600x800")
tabview = ctk.CTkTabview(master=app); tabview.pack(padx=20, pady=10, fill="both", expand=True)
tab_negociacoes = tabview.add("Calculadora de Negociações")
tab_reservas = tabview.add("Calculadora de Reservas")

#<editor-fold desc="Layout da Aba de Negociações">
# (código do layout da aba de negociações omitido para brevidade)
#</editor-fold>

#<editor-fold desc="Layout da Aba de Reservas">
tab_reservas.grid_columnconfigure(0, weight=1)
# --- LINHA 0: TÍTULO ---
res_label_titulo = ctk.CTkLabel(master=tab_reservas, text="Calculadora de Cotação de Reservas", font=("Roboto", 24, "bold"))
res_label_titulo.grid(row=0, column=0, padx=10, pady=(10, 15))
# --- LINHA 1: SELEÇÃO DE TIPO DE CONTRATO ---
res_combo_contrato = ctk.CTkComboBox(master=tab_reservas, values=["Antigo", "Novo"], command=update_reserva_ui)
res_combo_contrato.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
res_combo_contrato.set("Antigo")
# --- LINHA 2: FRAME PARA CONTRATO ANTIGO (INICIALMENTE VISÍVEL) ---
res_frame_antigo = ctk.CTkFrame(master=tab_reservas, fg_color="transparent")
res_frame_antigo.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
res_frame_antigo.grid_columnconfigure((0,1), weight=1)
res_combo_hotel = ctk.CTkComboBox(master=res_frame_antigo, values=["Bourbon Atibaia", "Bourbon Cataratas"], command=update_reserva_ui)
res_combo_hotel.grid(row=0, column=0, padx=(0,5), pady=5, sticky="ew")
res_combo_temporada = ctk.CTkComboBox(master=res_frame_antigo, values=[], command=update_reserva_ui)
res_combo_temporada.grid(row=0, column=1, padx=(5,0), pady=5, sticky="ew")
res_combo_acomodacao = ctk.CTkComboBox(master=res_frame_antigo, values=[])
res_combo_acomodacao.grid(row=1, column=0, columnspan=2, padx=0, pady=5, sticky="ew")

# --- LINHA 3: FRAME PARA CONTRATO NOVO (INICIALMENTE ESCONDIDO) ---
res_frame_novo = ctk.CTkFrame(master=tab_reservas, fg_color="transparent")
res_frame_novo.grid_columnconfigure((0,1), weight=1)
res_combo_tier_novo = ctk.CTkComboBox(master=res_frame_novo, values=["Style", "Select", "Sublime", "Luxury", "Sense"], command=update_reserva_ui)
res_combo_tier_novo.grid(row=0, column=0, padx=(0,5), pady=5, sticky="ew")
res_combo_hotel_novo = ctk.CTkComboBox(master=res_frame_novo, values=["Bourbon Atibaia", "Bourbon Cataratas"], command=update_reserva_ui)
res_combo_hotel_novo.grid(row=0, column=1, padx=(5,0), pady=5, sticky="ew")
res_combo_temporada_novo = ctk.CTkComboBox(master=res_frame_novo, values=[], command=update_reserva_ui)
res_combo_temporada_novo.grid(row=1, column=0, padx=(0,5), pady=5, sticky="ew")
res_combo_acomodacao_novo = ctk.CTkComboBox(master=res_frame_novo, values=[])
res_combo_acomodacao_novo.grid(row=1, column=1, padx=(5,0), pady=5, sticky="ew")
res_combo_fracionamento = ctk.CTkComboBox(master=res_frame_novo, values=["Abertura de Fracionamento", "Utilização de Fracionamento"])
res_combo_fracionamento.grid(row=2, column=0, columnspan=2, padx=0, pady=5, sticky="ew")

# --- LINHAS COMUNS (DATAS, HÓSPEDES, ETC.) ---
res_frame_datas = ctk.CTkFrame(master=tab_reservas, fg_color="transparent"); res_frame_datas.grid(row=4, column=0, sticky="ew"); res_frame_datas.grid_columnconfigure((0,1), weight=1)
res_entry_checkin = ctk.CTkEntry(master=res_frame_datas, placeholder_text="Check-in (dd/mm/aaaa)"); res_entry_checkin.grid(row=0, column=0, padx=(10,5), pady=5, sticky="ew")
res_entry_checkout = ctk.CTkEntry(master=res_frame_datas, placeholder_text="Check-out (dd/mm/aaaa)"); res_entry_checkout.grid(row=0, column=1, padx=(5,10), pady=5, sticky="ew")

res_frame_hospedes = ctk.CTkFrame(master=tab_reservas, fg_color="transparent"); res_frame_hospedes.grid(row=5, column=0, sticky="ew"); res_frame_hospedes.grid_columnconfigure((0,1,2), weight=1)
res_entry_adultos = ctk.CTkEntry(master=res_frame_hospedes, placeholder_text="Nº Adultos"); res_entry_adultos.grid(row=0, column=0, padx=(10,5), pady=5, sticky="ew")
res_entry_criancas_geral = ctk.CTkEntry(master=res_frame_hospedes, placeholder_text="Nº Crianças (<12 anos)")
res_frame_criancas_cataratas = ctk.CTkFrame(master=res_frame_hospedes, fg_color="transparent"); res_frame_criancas_cataratas.grid_columnconfigure((0,1,2), weight=1)
res_entry_criancas_0a2 = ctk.CTkEntry(master=res_frame_criancas_cataratas, placeholder_text="CHD 0-2"); res_entry_criancas_0a2.grid(row=0, column=0, sticky="ew")
res_entry_criancas_3a8 = ctk.CTkEntry(master=res_frame_criancas_cataratas, placeholder_text="CHD 3-8"); res_entry_criancas_3a8.grid(row=0, column=1, padx=5, sticky="ew")
res_entry_criancas_9a11 = ctk.CTkEntry(master=res_frame_criancas_cataratas, placeholder_text="CHD 9-11"); res_entry_criancas_9a11.grid(row=0, column=2, sticky="ew")
res_entry_noites_fds = ctk.CTkEntry(master=res_frame_hospedes, placeholder_text="Noites de Fim de Semana"); res_entry_noites_fds.grid(row=0, column=2, padx=(5,10), pady=5, sticky="ew")

res_frame_alim = ctk.CTkFrame(master=tab_reservas, fg_color="transparent"); res_frame_alim.grid(row=6, column=0, sticky="ew"); res_frame_alim.grid_columnconfigure((0,1), weight=1)
res_entry_valor_alim = ctk.CTkEntry(master=res_frame_alim, placeholder_text="Valor Alimentação/dia/adt"); res_entry_valor_alim.grid(row=0, column=0, padx=(10,5), pady=5, sticky="ew")
res_combo_pagto_alim = ctk.CTkComboBox(master=res_frame_alim, values=["Dinheiro", "Por Pontos"], command=toggle_valor_ponto_field); res_combo_pagto_alim.grid(row=0, column=1, padx=(5,10), pady=5, sticky="ew"); res_combo_pagto_alim.set("Dinheiro")
res_entry_valor_ponto = ctk.CTkEntry(master=res_frame_alim, placeholder_text="Valor do Ponto (ex: 0,17)")

res_entry_pontos_disponiveis = ctk.CTkEntry(master=tab_reservas, placeholder_text="Pontuação Disponível do Cliente")
res_entry_pontos_disponiveis.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

res_frame_botoes = ctk.CTkFrame(master=tab_reservas, fg_color="transparent"); res_frame_botoes.grid(row=8, column=0, pady=10); res_frame_botoes.grid_columnconfigure((0, 1), weight=1)
res_button_gerar = ctk.CTkButton(master=res_frame_botoes, text="Gerar Cotação", command=gerar_cotacao); res_button_gerar.grid(row=0, column=0, padx=(0, 5), sticky="ew")
res_button_limpar = ctk.CTkButton(master=res_frame_botoes, text="Limpar", command=limpar_campos_reserva, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE")); res_button_limpar.grid(row=0, column=1, padx=(5, 0), sticky="ew")

res_textbox_resultado = ctk.CTkTextbox(master=tab_reservas, font=("Consolas", 14), state="disabled", wrap="word")
res_textbox_resultado.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")
tab_reservas.grid_rowconfigure(9, weight=1)
#</editor-fold>

update_reserva_ui() # Chama a função para configurar o estado inicial da UI
app.mainloop()
#</editor-fold>