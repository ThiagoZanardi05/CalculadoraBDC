import customtkinter as ctk
import math
from datetime import datetime
import os
import sys

def resource_path(relative_path):
    """ Retorna o caminho absoluto para o recurso, funcionando tanto no modo de desenvolvimento quanto no PyInstaller """
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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
    neg_label_titulo.focus()
def toggle_entrada_fields():
    if neg_checkbox_entrada.get() == 1: neg_frame_entrada.grid(row=8, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="ew")
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
                             f"• {f'{qtd_parcelas_entrada}x parcelas de R$ {valor_parcela_entrada:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')} devem ser pagas para iniciar a negociação.\n"
                             f"------------------------------------------------------\n")
        saldo_para_renegociar = saldo_devedor - total_entrada; qtd_parcelas_disponiveis = qtd_parcelas_contrato_original - qtd_parcelas_entrada
        if qtd_parcelas_disponiveis < 6:
            exibir_resultado_negociacao(f"Erro: Após a entrada de {qtd_parcelas_entrada}x, "
                                     f"sobram apenas {qtd_parcelas_disponiveis} parcelas, "
                                     f"insuficiente para a negociação de 6 meses."); return
        tipo_produto = neg_combo_produto.get()
        valores_reduzidos = {"150.000": 350.00, "300.000": 500.00, "450.000 ou 600.000": 800.00, "1.000.000": 1000.00}
        if tipo_produto == "Selecione o Tipo de Produto": exibir_resultado_negociacao("Erro: Selecione um tipo de produto válido."); return
        valor_parcela_reduzida = valores_reduzidos[tipo_produto]; total_pago_na_reducao = 6 * valor_parcela_reduzida
        if saldo_para_renegociar < total_pago_na_reducao:
            exibir_resultado_negociacao(f"Proposta Inválida!\nO saldo restante após a entrada (R$ {f'{saldo_para_renegociar:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')}) "
                        f"é menor que o valor da redução (R$ {f'{total_pago_na_reducao:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')} )."); return
        saldo_devedor_apos_reducao = saldo_para_renegociar - total_pago_na_reducao
        parcelas_restantes_normais = qtd_parcelas_disponiveis - 6
        if parcelas_restantes_normais <= 0:
            proposta_renegociacao = (f"PROPOSTA DE RENEGOCIAÇÃO:\n\n"
                                    f"• As 6 parcelas de R$ {f'{valor_parcela_reduzida:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')} quitam a dívida.")
        else:
            valor_base_nova_parcela = saldo_devedor_apos_reducao / parcelas_restantes_normais
            parcela_padrao_arredondada = math.floor(valor_base_nova_parcela)
            ultima_parcela_ajuste = saldo_devedor_apos_reducao - (parcela_padrao_arredondada * (parcelas_restantes_normais - 1))
            proposta_renegociacao = (f"PROPOSTA DE RENEGOCIAÇÃO:\n\n"
                                    f"• 6x parcelas de R$ {f'{valor_parcela_reduzida:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')} \n"
                                    f"• {parcelas_restantes_normais - 1}x parcelas de R$ {f'{parcela_padrao_arredondada:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')} \n"
                                    f"• 1x parcela de ajuste de R$ {f'{ultima_parcela_ajuste:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')}")
        exibir_resultado_negociacao(texto_entrada + proposta_renegociacao)
    except (ValueError, KeyError, TypeError):
        exibir_resultado_negociacao("Erro: Verifique se todos os campos estão preenchidos com números válidos.")
def exibir_resultado_negociacao(texto):
    neg_textbox_resultado.configure(state="normal"); neg_textbox_resultado.delete("1.0", "end")
    neg_textbox_resultado.insert("1.0", texto); neg_textbox_resultado.configure(state="disabled")
#</editor-fold>

#<editor-fold desc="Funções da Calculadora de Reservas (Aba 2)">
def update_reserva_ui(*args):
    contrato = res_combo_contrato.get()
    
    res_frame_antigo.grid_forget()
    res_frame_novo.grid_forget()

    hotel_selecionado_agora = ""
    if contrato == "Novo":
        hotel_selecionado_agora = res_combo_hotel_novo.get()
    else: # Contrato Antigo
        hotel_selecionado_agora = res_combo_hotel.get()

    # LÓGICA CORRIGIDA PARA EXPANDIR O CAMPO DE ATIBAIA
    if hotel_selecionado_agora == "Bourbon Cataratas":
        res_entry_criancas_geral.grid_forget()
        # O frame de cataratas se expande e mostra os 3 campos internos
        res_frame_criancas_cataratas.grid(row=0, column=0, sticky="ew")
    else: # Bourbon Atibaia ou nenhum hotel selecionado
        res_frame_criancas_cataratas.grid_forget()
        # O campo geral de crianças agora se expande para preencher o container
        res_entry_criancas_geral.grid(row=0, column=0, sticky="ew")

    if contrato == "Novo":
        res_frame_novo.grid(row=0, column=0, sticky="ew")
        
        selected_hotel_novo = res_combo_hotel_novo.get()
        selected_tier = res_combo_tier_novo.get()
        hotel_key_novo = "Bourbon Atibaia" if selected_hotel_novo == "Bourbon Atibaia" else "Bourbon Cataratas"
        
        if selected_tier == "Selecione o Tier":
            res_combo_temporada_novo.configure(values=[], state="disabled")
            res_combo_acomodacao_novo.configure(values=[], state="disabled")
        else:
            allowed_seasons = REGRAS_TIER_NOVO.get(selected_tier, [])
            available_seasons = [s for s in TABELA_PONTOS_NOVO.get(hotel_key_novo, {}).keys() if any(allowed in s for allowed in allowed_seasons)]
            res_combo_temporada_novo.configure(values=available_seasons, state="normal")
            
            all_acomodacoes_novo = set()
            for temp in available_seasons: all_acomodacoes_novo.update(TABELA_PONTOS_NOVO.get(hotel_key_novo, {}).get(temp, {}).keys())
            acomodacoes_list_novo = sorted(list(all_acomodacoes_novo))
            res_combo_acomodacao_novo.configure(values=acomodacoes_list_novo, state="normal")

        if res_combo_temporada_novo.get() not in res_combo_temporada_novo.cget("values"): res_combo_temporada_novo.set("Selecione a Temporada")
        if res_combo_acomodacao_novo.get() not in res_combo_acomodacao_novo.cget("values"): res_combo_acomodacao_novo.set("Selecione a Acomodação")

    else: # Contrato Antigo
        res_frame_novo.grid_forget()
        res_frame_antigo.grid(row=0, column=0, sticky="ew")

        selected_hotel_antigo = res_combo_hotel.get()
        if selected_hotel_antigo == "Selecione o Hotel":
            res_combo_temporada.configure(values=[], state="disabled")
            res_combo_acomodacao.configure(values=[], state="disabled")
        else:
            temporadas_antigo = list(TABELA_PONTOS_ANTIGO.get(selected_hotel_antigo, {}).keys())
            res_combo_temporada.configure(values=temporadas_antigo, state="normal")
            
            all_acomodacoes_antigo = set()
            for temporada_data in TABELA_PONTOS_ANTIGO.get(selected_hotel_antigo, {}).values(): all_acomodacoes_antigo.update(temporada_data.keys())
            acomodacoes_list_antigo = sorted(list(all_acomodacoes_antigo))
            res_combo_acomodacao.configure(values=acomodacoes_list_antigo, state="normal")

        if res_combo_temporada.get() not in res_combo_temporada.cget("values"): res_combo_temporada.set("Selecione a Temporada")
        if res_combo_acomodacao.get() not in res_combo_acomodacao.cget("values"): res_combo_acomodacao.set("Selecione a Acomodação")

def toggle_valor_ponto_field(*args):
    if res_combo_pagto_alim.get() == "Por Pontos":
        res_entry_valor_ponto.grid(row=2, column=2, padx=(5, 15), pady=(0,15), sticky="ew")
    else:
        res_entry_valor_ponto.grid_forget()

def limpar_campos_reserva():
    res_combo_contrato.set("Antigo")
    res_combo_hotel.set("Selecione o Hotel")
    res_combo_temporada.set("Selecione a Temporada")
    res_combo_acomodacao.set("Selecione a Acomodação")
    res_combo_tier_novo.set("Selecione o Tier")
    res_combo_hotel_novo.set("Selecione o Hotel")
    res_combo_temporada_novo.set("Selecione a Temporada")
    res_combo_acomodacao_novo.set("Selecione a Acomodação")
    res_combo_fracionamento.set("Abertura de Fracionamento")
    
    for entry in [res_entry_checkin, res_entry_checkout, res_entry_adultos, res_entry_noites_fds, res_entry_criancas_geral, res_entry_criancas_0a2, res_entry_criancas_3a8, res_entry_criancas_9a11, res_entry_valor_alim, res_entry_valor_ponto, res_entry_pontos_disponiveis]: entry.delete(0, 'end')
    
    res_combo_pagto_alim.set("Dinheiro")
    toggle_valor_ponto_field()
    update_reserva_ui()
    exibir_resultado_reserva("")
    res_label_titulo.focus()

def gerar_cotacao():
    try:
        contrato_tipo = res_combo_contrato.get()
        checkin_str, checkout_str = res_entry_checkin.get(), res_entry_checkout.get()
        checkin_data = datetime.strptime(checkin_str, '%d/%m/%Y'); checkout_data = datetime.strptime(checkout_str, '%d/%m/%Y')
        total_noites = (checkout_data - checkin_data).days
        if total_noites <= 0: exibir_resultado_reserva("Erro: Data de Check-out inválida."); return
        adultos = int(res_entry_adultos.get() or 0)
        noites_fds = int(res_entry_noites_fds.get() or 0)
        
        pontos_disponiveis_str = res_entry_pontos_disponiveis.get()
        if ',' in pontos_disponiveis_str:
            pontos_disponiveis_str = pontos_disponiveis_str.replace('.', '').replace(',', '.')
        pontos_disponiveis = int(float(pontos_disponiveis_str or 0))

        if contrato_tipo == "Antigo":
            hotel, acomodacao, temporada = res_combo_hotel.get(), res_combo_acomodacao.get(), res_combo_temporada.get()
            if not all([hotel != "Selecione o Hotel", acomodacao != "Selecione a Acomodação", temporada != "Selecione a Temporada"]): 
                exibir_resultado_reserva("Erro: Preencha todos os campos do Contrato Antigo."); return
            
            total_chd = 0
            if hotel == "Bourbon Cataratas":
                criancas_0a2, criancas_3a8, criancas_9a11 = int(res_entry_criancas_0a2.get() or 0), int(res_entry_criancas_3a8.get() or 0), int(res_entry_criancas_9a11.get() or 0)
                total_chd = criancas_0a2 + criancas_3a8 + criancas_9a11
            else: total_chd = int(res_entry_criancas_geral.get() or 0)
            
            if (adultos + total_chd) > (5 if "Familia" in acomodacao else 4):
                exibir_resultado_reserva(f"Erro: Ocupação excede o limite para esta categoria."); return

            pontos_semana = TABELA_PONTOS_ANTIGO[hotel][temporada][acomodacao]
            total_pontos_estadia = math.ceil(((pontos_semana / 7) * total_noites) + ((pontos_semana / 7) * 0.20 * noites_fds))
            
            texto_resultado = f"*{checkin_str} a {checkout_str}* ({total_noites} noites)\n\n"
            texto_resultado += f"Hotel: *{hotel}*\n"
            texto_resultado += f"Categoria: *{acomodacao}* ({adultos} adt + {total_chd} chd)\n"
            texto_resultado += f"Pontuação: *{f'{total_pontos_estadia:,}'.replace(',', '.')} Pontos*\n"

            valor_alim_str = res_entry_valor_alim.get()
            if valor_alim_str:
                if ',' in valor_alim_str: valor_alim_str = valor_alim_str.replace('.', '').replace(',', '.')
                valor_alim_dia_adulto = float(valor_alim_str)

                total_alim_dinheiro = 0
                if hotel == "Bourbon Cataratas":
                    pagantes_inteira = adultos + criancas_9a11
                    pagantes_meia = criancas_3a8
                    custo_diario = (pagantes_inteira * valor_alim_dia_adulto) + (pagantes_meia * valor_alim_dia_adulto / 2)
                    total_alim_dinheiro = custo_diario * total_noites
                else: 
                    total_alim_dinheiro = valor_alim_dia_adulto * adultos * total_noites
                
                if res_combo_pagto_alim.get() == "Dinheiro": texto_resultado += f"Alimentação: *R$ {f'{total_alim_dinheiro:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')}*\n"
                else:
                    valor_ponto_str = res_entry_valor_ponto.get().replace(',', '.')
                    valor_ponto = float(valor_ponto_str)
                    total_pontos_alim = math.ceil(total_alim_dinheiro / valor_ponto)
                    texto_resultado += f"Alimentação: *{f'{total_pontos_alim:,}'.replace(',', '.')} Pontos*\n"
            
            texto_taxa = "Taxa de Utilização: *Sem taxa de utilização*\n"
            if hotel == "Bourbon Cataratas":
                taxa_diaria = 58.00
                if "Triplo" in acomodacao: taxa_diaria = 86.00
                elif "Familia" in acomodacao: taxa_diaria = 116.00
                taxa_total = taxa_diaria * total_noites
                texto_taxa = f"Taxa de Utilização: *R$ {f'{taxa_total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')}*\n"
            
            texto_resultado += texto_taxa
            texto_resultado += f"Pontuação disponível: {f'{pontos_disponiveis:,}'.replace(',', '.')} pontos\n\n"
            texto_resultado += "Gostaria de seguir com a reserva?"
            exibir_resultado_reserva(texto_resultado)

        elif contrato_tipo == "Novo":
            hotel_ui, tier, temporada, acomodacao, tipo_uso = res_combo_hotel_novo.get(), res_combo_tier_novo.get(), res_combo_temporada_novo.get(), res_combo_acomodacao_novo.get(), res_combo_fracionamento.get()
            hotel_key = "Bourbon Atibaia" if hotel_ui == "Bourbon Atibaia" else "Bourbon Cataratas"

            if not all([hotel_ui != "Selecione o Hotel", tier != "Selecione o Tier", temporada != "Selecione a Temporada", acomodacao != "Selecione a Acomodação"]):
                exibir_resultado_reserva("Erro: Preencha todos os campos do Contrato Novo."); return
            
            total_chd = 0
            if hotel_ui == "Bourbon Cataratas":
                criancas_0a2, criancas_3a8, criancas_9a11 = int(res_entry_criancas_0a2.get() or 0), int(res_entry_criancas_3a8.get() or 0), int(res_entry_criancas_9a11.get() or 0)
                total_chd = criancas_0a2 + criancas_3a8 + criancas_9a11
            else:
                total_chd = int(res_entry_criancas_geral.get() or 0)
            
            if (adultos + total_chd) > (5 if "Familia" in acomodacao else 4):
                exibir_resultado_reserva(f"Erro: Ocupação excede o limite para esta categoria."); return

            pontuacao_hospedagem = TABELA_PONTOS_NOVO[hotel_key][temporada][acomodacao] if tipo_uso == "Abertura de Fracionamento" else 0

            total_alim_reais = 0
            valor_alim_str = res_entry_valor_alim.get()
            if valor_alim_str:
                if ',' in valor_alim_str: valor_alim_str = valor_alim_str.replace('.', '').replace(',', '.')
                valor_alim_dia_adulto = float(valor_alim_str)

                if hotel_ui == "Bourbon Cataratas":
                    pagantes_inteira = adultos + criancas_9a11
                    pagantes_meia = criancas_3a8
                    custo_diario = (pagantes_inteira * valor_alim_dia_adulto) + (pagantes_meia * valor_alim_dia_adulto / 2)
                    total_alim_reais = custo_diario * total_noites
                else: 
                    total_alim_reais = valor_alim_dia_adulto * adultos * total_noites
            
            taxa_diaria = 58.00
            if "Triplo" in acomodacao: taxa_diaria = 86.00
            elif "Familia" in acomodacao: taxa_diaria = 116.00
            total_taxa_utilizacao_reais = taxa_diaria * total_noites
            total_taxa_clube_reais = total_alim_reais + total_taxa_utilizacao_reais
            
            pontos_taxa_clube = 0; texto_taxa_clube = ""
            if res_combo_pagto_alim.get() == "Dinheiro":
                texto_taxa_clube = f"Taxa Clube: *R$ {f'{total_taxa_clube_reais:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')}*\n"
            else:
                valor_ponto_str = res_entry_valor_ponto.get().replace(',', '.')
                valor_ponto = float(valor_ponto_str)
                pontos_taxa_clube = math.ceil(total_taxa_clube_reais / valor_ponto)
                texto_taxa_clube = f"Taxa Clube: *{f'{pontos_taxa_clube:,}'.replace(',', '.')} Pontos*\n"
            
            total_pontos_necessarios = pontuacao_hospedagem + pontos_taxa_clube
            
            texto_resultado = f"Período: {checkin_str} a {checkout_str} ({total_noites} diárias)\nHotel: {hotel_ui}\n\n"
            texto_resultado += f"Quarto - {tipo_uso}\nCategoria: {acomodacao}\nOcupação: {adultos} adultos e {total_chd} crianças\n"
            texto_resultado += f"Pontuação hospedagem: *{f'{pontuacao_hospedagem:,}'.replace(',', '.')} pontos*\n"
            texto_resultado += texto_taxa_clube
            texto_resultado += f"\n*Total de pontos necessários: {f'{total_pontos_necessarios:,}'.replace(',', '.')} pontos*"
            exibir_resultado_reserva(texto_resultado)

    except (ValueError, KeyError, TypeError) as e:
        exibir_resultado_reserva(f"Erro nos dados: Verifique se todos os campos estão preenchidos corretamente.\nDetalhe: {e}")
def exibir_resultado_reserva(texto):
    res_textbox_resultado.configure(state="normal"); res_textbox_resultado.delete("1.0", "end")
    res_textbox_resultado.insert("1.0", texto); res_textbox_resultado.configure(state="disabled")

def initialize_ui():
    """Chama as funções de limpeza depois que a janela principal já foi criada."""
    limpar_campos_negociacao()
    limpar_campos_reserva()
#</editor-fold>

#<editor-fold desc="Layout da Aplicação Principal">
# --- CONFIGURAÇÕES DE ESTILO ---
ctk.set_appearance_mode("dark")

FONT_FAMILY = "Roboto"
TITLE_FONT = (FONT_FAMILY, 26, "bold")
SECTION_TITLE_FONT = (FONT_FAMILY, 16, "bold")
LABEL_FONT = (FONT_FAMILY, 13)
BUTTON_FONT = (FONT_FAMILY, 14, "bold")
SMALL_LABEL_FONT = (FONT_FAMILY, 12)

PRIMARY_COLOR = "#0D6ABF" # Azul Bourbon
SECONDARY_COLOR = "#4A4A4A" # Cinza para botões secundários
FRAME_COLOR = "#2B2B2B"
BG_COLOR = "#242424"
TEXT_COLOR = "#DCE4EE"

# --- JANELA PRINCIPAL ---
app = ctk.CTk()
app.title("Calculadora de Cotações | Bourbon Club")
app.geometry("650x700")
app.resizable(False, False)
# --- Define o Ícone da Aplicação (de forma segura) ---
try:
    icon_path = resource_path("icone.ico")
    app.iconbitmap(icon_path)
except Exception as e:
    print(f"Erro ao carregar o ícone: {e}")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

tabview = ctk.CTkTabview(
    master=app,
    anchor="w",
    fg_color=BG_COLOR,
    segmented_button_selected_color=PRIMARY_COLOR,
    segmented_button_selected_hover_color="#0A5599",
    segmented_button_unselected_color=SECONDARY_COLOR
)
tabview.pack(padx=15, pady=10, fill="both", expand=True)

tab_negociacoes = tabview.add("Negociações")
tab_reservas = tabview.add("Reservas")

tab_negociacoes.grid_columnconfigure(0, weight=1)
tab_reservas.grid_columnconfigure(0, weight=1)

#<editor-fold desc="Layout da Aba de Negociações">
# --- FRAME PRINCIPAL ---
neg_main_frame = ctk.CTkFrame(tab_negociacoes, fg_color="transparent")
neg_main_frame.pack(fill="both", expand=True, padx=5, pady=5)
neg_main_frame.grid_columnconfigure(0, weight=1)
neg_main_frame.grid_rowconfigure(2, weight=1)

# --- TÍTULO ---
neg_label_titulo = ctk.CTkLabel(neg_main_frame, text="Calculadora de Negociações", font=TITLE_FONT, text_color=PRIMARY_COLOR)
neg_label_titulo.grid(row=0, column=0, padx=10, pady=(10, 25), sticky="ew")

# --- FRAME DE INPUTS ---
neg_inputs_frame = ctk.CTkFrame(neg_main_frame, fg_color=FRAME_COLOR, corner_radius=10)
neg_inputs_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
neg_inputs_frame.grid_columnconfigure((0, 1), weight=1)

ctk.CTkLabel(neg_inputs_frame, text="Tipo de Produto do Sócio", font=LABEL_FONT, anchor="w").grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 5), sticky="ew")
neg_combo_produto = ctk.CTkComboBox(neg_inputs_frame, height=35, values=["150.000", "300.000", "450.000 ou 600.000", "1.000.000"], button_color=PRIMARY_COLOR, corner_radius=8)
neg_combo_produto.grid(row=1, column=0, columnspan=2, padx=15, pady=(0, 10), sticky="ew")

ctk.CTkLabel(neg_inputs_frame, text="Valor Total do Contrato", font=LABEL_FONT, anchor="w").grid(row=2, column=0, padx=15, pady=(5, 5), sticky="ew")
neg_entry_valor_total = ctk.CTkEntry(neg_inputs_frame, height=35, corner_radius=8)
neg_entry_valor_total.grid(row=3, column=0, padx=(15, 5), pady=(0, 10), sticky="ew")

ctk.CTkLabel(neg_inputs_frame, text="Valor Já Pago", font=LABEL_FONT, anchor="w").grid(row=2, column=1, padx=(5, 15), pady=(5, 5), sticky="ew")
neg_entry_valor_pago = ctk.CTkEntry(neg_inputs_frame, height=35, corner_radius=8)
neg_entry_valor_pago.grid(row=3, column=1, padx=(5, 15), pady=(0, 10), sticky="ew")

ctk.CTkLabel(neg_inputs_frame, text="Quantidade Total de Parcelas", font=LABEL_FONT, anchor="w").grid(row=4, column=0, columnspan=2, padx=15, pady=(5, 5), sticky="ew")
neg_entry_qtd_parcelas = ctk.CTkEntry(neg_inputs_frame, height=35, corner_radius=8)
neg_entry_qtd_parcelas.grid(row=5, column=0, columnspan=2, padx=15, pady=(0, 15), sticky="ew")

neg_checkbox_entrada = ctk.CTkCheckBox(neg_inputs_frame, text="O cliente dará uma entrada?", command=toggle_entrada_fields, checkbox_height=20, checkbox_width=20, corner_radius=15, fg_color=PRIMARY_COLOR)
neg_checkbox_entrada.grid(row=6, column=0, columnspan=2, padx=15, pady=10, sticky="w")
neg_frame_entrada = ctk.CTkFrame(neg_inputs_frame, fg_color="transparent")
neg_frame_entrada.grid(row=7, column=0, columnspan=2, padx=15, pady=(0, 15), sticky="ew")
neg_frame_entrada.grid_columnconfigure((0,1), weight=1)
neg_entry_qtd_entrada = ctk.CTkEntry(master=neg_frame_entrada, placeholder_text="Qtd. parcelas entrada", height=35, corner_radius=8)
neg_entry_qtd_entrada.grid(row=0, column=0, padx=(0,5), pady=5, sticky="ew")
neg_entry_valor_entrada = ctk.CTkEntry(master=neg_frame_entrada, placeholder_text="Valor parcela entrada", height=35, corner_radius=8)
neg_entry_valor_entrada.grid(row=0, column=1, padx=(5,0), pady=5, sticky="ew")
neg_frame_entrada.grid_remove()

# --- RESULTADO ---
neg_textbox_resultado = ctk.CTkTextbox(neg_main_frame, font=("Consolas", 14), state="disabled", wrap="word", corner_radius=10, fg_color=FRAME_COLOR)
neg_textbox_resultado.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# --- BOTÕES ---
neg_frame_botoes = ctk.CTkFrame(neg_main_frame, fg_color="transparent")
neg_frame_botoes.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
neg_frame_botoes.grid_columnconfigure((0, 1), weight=1)
neg_button_gerar = ctk.CTkButton(neg_frame_botoes, text="Gerar Proposta", command=calcular_proposta, height=40, font=BUTTON_FONT, corner_radius=8, fg_color=PRIMARY_COLOR, hover_color="#0A5599")
neg_button_gerar.grid(row=0, column=0, padx=(0, 10), sticky="ew")
neg_button_limpar = ctk.CTkButton(neg_frame_botoes, text="Limpar", command=limpar_campos_negociacao, height=40, font=BUTTON_FONT, corner_radius=8, fg_color="transparent", border_color=SECONDARY_COLOR, border_width=2, hover_color=FRAME_COLOR)
neg_button_limpar.grid(row=0, column=1, padx=(10, 0), sticky="ew")

# --- CRÉDITOS ---
neg_label_creditos = ctk.CTkLabel(neg_main_frame, text="Feito por Thiago Zanardi", font=(FONT_FAMILY, 10), text_color="gray50")
neg_label_creditos.grid(row=4, column=0, padx=10, pady=(5, 10))
#</editor-fold>

#<editor-fold desc="Layout da Aba de Reservas">
# --- FRAME PRINCIPAL COM SCROLL ---
res_main_frame = ctk.CTkScrollableFrame(tab_reservas, fg_color="transparent", label_text=None)
res_main_frame.pack(fill="both", expand=True, padx=0, pady=0)
res_main_frame.grid_columnconfigure(0, weight=1)

# --- TÍTULO ---
res_label_titulo = ctk.CTkLabel(res_main_frame, text="Cotação de Reservas", font=TITLE_FONT, text_color=PRIMARY_COLOR)
res_label_titulo.grid(row=0, column=0, padx=10, pady=(10, 20), sticky="ew")

# --- FRAME OPÇÕES DO CONTRATO ---
res_contract_options_frame = ctk.CTkFrame(res_main_frame, fg_color=FRAME_COLOR, corner_radius=10)
res_contract_options_frame.grid(row=1, column=0, padx=10, pady=10, sticky="new")
res_contract_options_frame.grid_columnconfigure(0, weight=1)
ctk.CTkLabel(res_contract_options_frame, text="Opções do Contrato", font=SECTION_TITLE_FONT, anchor="w").grid(row=0, column=0, padx=15, pady=(15, 10), sticky="ew")
res_combo_contrato = ctk.CTkComboBox(res_contract_options_frame, values=["Antigo", "Novo"], command=update_reserva_ui, height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_contrato.grid(row=1, column=0, padx=15, pady=(0, 10), sticky="ew")
res_content_frame = ctk.CTkFrame(res_contract_options_frame, fg_color="transparent")
res_content_frame.grid(row=2, column=0, sticky="ew", padx=15, pady=(0, 15))
res_content_frame.grid_columnconfigure(0, weight=1)
res_frame_antigo = ctk.CTkFrame(res_content_frame, fg_color="transparent")
res_frame_antigo.grid_columnconfigure((0,1), weight=1)
res_combo_hotel = ctk.CTkComboBox(res_frame_antigo, values=["Bourbon Atibaia", "Bourbon Cataratas"], command=update_reserva_ui, height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_hotel.grid(row=0, column=0, padx=(0,5), pady=5, sticky="ew")
res_combo_temporada = ctk.CTkComboBox(res_frame_antigo, values=[], command=update_reserva_ui, height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_temporada.grid(row=0, column=1, padx=(5,0), pady=5, sticky="ew")
res_combo_acomodacao = ctk.CTkComboBox(res_frame_antigo, values=[], height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_acomodacao.grid(row=1, column=0, columnspan=2, padx=0, pady=5, sticky="ew")
res_frame_novo = ctk.CTkFrame(res_content_frame, fg_color="transparent")
res_frame_novo.grid_columnconfigure((0,1), weight=1)
res_combo_tier_novo = ctk.CTkComboBox(res_frame_novo, values=list(REGRAS_TIER_NOVO.keys()), command=update_reserva_ui, height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_tier_novo.grid(row=0, column=0, padx=(0,5), pady=5, sticky="ew")
res_combo_hotel_novo = ctk.CTkComboBox(res_frame_novo, values=["Bourbon Atibaia", "Bourbon Cataratas"], command=update_reserva_ui, height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_hotel_novo.grid(row=0, column=1, padx=(5,0), pady=5, sticky="ew")
res_combo_temporada_novo = ctk.CTkComboBox(res_frame_novo, values=[], height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_temporada_novo.grid(row=1, column=0, padx=(0,5), pady=5, sticky="ew")
res_combo_acomodacao_novo = ctk.CTkComboBox(res_frame_novo, values=[], height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_acomodacao_novo.grid(row=1, column=1, padx=(5,0), pady=5, sticky="ew")
res_combo_fracionamento = ctk.CTkComboBox(res_frame_novo, values=["Abertura de Fracionamento", "Utilização de Fracionamento"], height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_fracionamento.grid(row=2, column=0, columnspan=2, padx=0, pady=5, sticky="ew")

# --- FRAME DETALHES DA ESTADIA ---
res_details_frame = ctk.CTkFrame(res_main_frame, fg_color=FRAME_COLOR, corner_radius=10)
res_details_frame.grid(row=2, column=0, padx=10, pady=10, sticky="new")
res_details_frame.grid_columnconfigure((0, 1), weight=1)

ctk.CTkLabel(res_details_frame, text="Detalhes da Estadia", font=SECTION_TITLE_FONT, anchor="w").grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10), sticky="ew")

ctk.CTkLabel(res_details_frame, text="Check-in", font=LABEL_FONT, anchor="w").grid(row=1, column=0, padx=15, pady=(5, 5), sticky="ew")
res_entry_checkin = ctk.CTkEntry(res_details_frame, placeholder_text="dd/mm/aaaa", height=35, corner_radius=8)
res_entry_checkin.grid(row=2, column=0, padx=15, pady=(0,10), sticky="ew")

ctk.CTkLabel(res_details_frame, text="Check-out", font=LABEL_FONT, anchor="w").grid(row=1, column=1, padx=15, pady=(5, 5), sticky="ew")
res_entry_checkout = ctk.CTkEntry(res_details_frame, placeholder_text="dd/mm/aaaa", height=35, corner_radius=8)
res_entry_checkout.grid(row=2, column=1, padx=15, pady=(0,10), sticky="ew")

ctk.CTkLabel(res_details_frame, text="Nº Adultos", font=LABEL_FONT, anchor="w").grid(row=3, column=0, columnspan=2, padx=15, pady=(10,5), sticky="ew")
res_entry_adultos = ctk.CTkEntry(res_details_frame, height=35, corner_radius=8)
res_entry_adultos.grid(row=4, column=0, columnspan=2, padx=15, pady=(0,10), sticky="ew")

ctk.CTkLabel(res_details_frame, text="Crianças", font=LABEL_FONT, anchor="w").grid(row=5, column=0, columnspan=2, padx=15, pady=(10,5), sticky="ew")

# Container para os widgets de crianças, para que eles apareçam/desapareçam no lugar certo
res_criancas_container_geral = ctk.CTkFrame(res_details_frame, fg_color="transparent")
res_criancas_container_geral.grid(row=6, column=0, columnspan=2, padx=15, pady=0, sticky="ew")
res_criancas_container_geral.grid_columnconfigure(0, weight=1)

ctk.CTkLabel(res_details_frame, text="Noites de Fim de Semana", font=LABEL_FONT, anchor="w").grid(row=7, column=0, columnspan=2, padx=15, pady=(10,5), sticky="ew")
res_entry_noites_fds = ctk.CTkEntry(res_details_frame, height=35, corner_radius=8)
res_entry_noites_fds.grid(row=8, column=0, columnspan=2, padx=15, pady=(0,15), sticky="ew")

# Widgets de Crianças agora pertencem ao novo container
res_entry_criancas_geral = ctk.CTkEntry(master=res_criancas_container_geral, placeholder_text="Nº Crianças (<12 anos)", height=35, corner_radius=8)
res_frame_criancas_cataratas = ctk.CTkFrame(master=res_criancas_container_geral, fg_color="transparent")
res_frame_criancas_cataratas.grid_columnconfigure((0,1,2), weight=1)

ctk.CTkLabel(res_frame_criancas_cataratas, text="CHD 0-2Y", font=SMALL_LABEL_FONT).grid(row=0, column=0, sticky="s", padx=2, pady=0)
ctk.CTkLabel(res_frame_criancas_cataratas, text="CHD 3-8Y", font=SMALL_LABEL_FONT).grid(row=0, column=1, sticky="s", padx=2, pady=0)
ctk.CTkLabel(res_frame_criancas_cataratas, text="CHD 9-11Y", font=SMALL_LABEL_FONT).grid(row=0, column=2, sticky="s", padx=2, pady=0)

res_entry_criancas_0a2 = ctk.CTkEntry(master=res_frame_criancas_cataratas, placeholder_text="", height=35, corner_radius=8); res_entry_criancas_0a2.grid(row=1, column=0, padx=(0,5), sticky="ew")
res_entry_criancas_3a8 = ctk.CTkEntry(master=res_frame_criancas_cataratas, placeholder_text="", height=35, corner_radius=8); res_entry_criancas_3a8.grid(row=1, column=1, padx=5, sticky="ew")
res_entry_criancas_9a11 = ctk.CTkEntry(master=res_frame_criancas_cataratas, placeholder_text="", height=35, corner_radius=8); res_entry_criancas_9a11.grid(row=1, column=2, padx=(5,0), sticky="ew")

# --- FRAME CUSTOS ADICIONAIS ---
res_costs_frame = ctk.CTkFrame(res_main_frame, fg_color=FRAME_COLOR, corner_radius=10)
res_costs_frame.grid(row=3, column=0, padx=10, pady=10, sticky="new")
res_costs_frame.grid_columnconfigure((0, 1), weight=1)
ctk.CTkLabel(res_costs_frame, text="Custos Adicionais", font=SECTION_TITLE_FONT, anchor="w").grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10), sticky="ew")
ctk.CTkLabel(res_costs_frame, text="Valor Alimentação/dia/adt", font=LABEL_FONT, anchor="w").grid(row=1, column=0, padx=15, pady=(5,5), sticky="ew")
res_entry_valor_alim = ctk.CTkEntry(res_costs_frame, height=35, corner_radius=8)
res_entry_valor_alim.grid(row=2, column=0, padx=(15,5), pady=(0,15), sticky="ew")
ctk.CTkLabel(res_costs_frame, text="Pagamento Alimentação", font=LABEL_FONT, anchor="w").grid(row=1, column=1, padx=(5,15), pady=(5,5), sticky="ew")
res_combo_pagto_alim = ctk.CTkComboBox(res_costs_frame, values=["Dinheiro", "Por Pontos"], command=toggle_valor_ponto_field, height=35, button_color=PRIMARY_COLOR, corner_radius=8)
res_combo_pagto_alim.grid(row=2, column=1, padx=(5,15), pady=(0,15), sticky="ew")
res_entry_valor_ponto = ctk.CTkEntry(res_costs_frame, placeholder_text="Valor do Ponto (ex: 0.17)", height=35, corner_radius=8)
ctk.CTkLabel(res_costs_frame, text="Pontuação Disponível do Cliente", font=LABEL_FONT, anchor="w").grid(row=3, column=0, columnspan=2, padx=15, pady=(5,5), sticky="ew")
res_entry_pontos_disponiveis = ctk.CTkEntry(res_costs_frame, height=35, corner_radius=8)
res_entry_pontos_disponiveis.grid(row=4, column=0, columnspan=2, padx=15, pady=(0,15), sticky="ew")

# --- RESULTADO ---
res_textbox_resultado = ctk.CTkTextbox(res_main_frame, font=("Consolas", 14), state="disabled", wrap="word", corner_radius=10, fg_color=FRAME_COLOR, height=250)
res_textbox_resultado.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

# --- BOTÕES ---
res_frame_botoes = ctk.CTkFrame(res_main_frame, fg_color="transparent")
res_frame_botoes.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
res_frame_botoes.grid_columnconfigure((0, 1), weight=1)
res_button_gerar = ctk.CTkButton(master=res_frame_botoes, text="Gerar Cotação", command=gerar_cotacao, height=40, font=BUTTON_FONT, corner_radius=8, fg_color=PRIMARY_COLOR, hover_color="#0A5599")
res_button_gerar.grid(row=0, column=0, padx=(0, 10), sticky="ew")
res_button_limpar = ctk.CTkButton(master=res_frame_botoes, text="Limpar", command=limpar_campos_reserva, height=40, font=BUTTON_FONT, corner_radius=8, fg_color="transparent", border_color=SECONDARY_COLOR, border_width=2, hover_color=FRAME_COLOR)
res_button_limpar.grid(row=0, column=1, padx=(10, 0), sticky="ew")

#</editor-fold>

app.after(10, initialize_ui)
app.mainloop()
#</editor-fold>