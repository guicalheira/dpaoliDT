global css body c:warm2 bg:warm8 ff:Arial inset:0 d:vcc bg:gray-100 h:100%  box-sizing:border-box

tag Dashboard
  	
	activeTab = "rotinas"
	
	def switchTab(tab)
		activeTab = tab
	
	<self>
		css w:100% d:flex fld:row g:10px
		<.sidebar>
			css w:20% bg:gray7 c:white p:4
			<h2> "Eventos"
			<.events>
				css h:75% oy:auto
				<p.event-item> "[12:00] Nova requisição processada"
				<p.event-item> "[12:05] Erro em arquivo X"
				<p.event-item> "[12:10] Cadastro de cliente concluído"
		
		<.main>
			css   p:4
			<.request-box>
				css bg:white sh:0 2px 4px rgba(0,0,0,0.1) rd:5 p:3 mb:3
				<h3> "Janela Interativa de Requisições"
				<textarea rows=3 placeholder="Digite a solicitação..."><textarea>
				<button> "Enviar"
			
			<.tabs>
				css  d:flex bb:10px solid gray4 mb:3 g:10px
				<button.tab-button @click=switchTab("rotinas") .activeTab =("rotinas" ? "active" : "")> "Rotinas"
				<button.tab-button @click=switchTab("logs") .activeTab =("logs" ? "active" : "")> "Logs"
			if activeTab = "rotinas"
				<.tab-content >
					css bg:white p:3 sh:0 2px 4px rgba(0,0,0,0.1) rd:5 
					<h3> "Rotinas"
					<ul>
						<li> "Execução de Cadastro"
						<li> "Monitoramento de Arquivos"
						<li> "Verificação de Logs"
			if activeTab = "logs"
				<.tab-content >
					css bg:white p:3 sh:0 2px 4px rgba(0,0,0,0.1) rd:5
					<h3> "Logs"
					<p> "[12:00] Processando requisição..."
					<p> "[12:01] Arquivo localizado"
					<p> "[12:02] Dados extraídos"
		
	css 
		.tab-button  padding: 10px; border: 1px solid #ccc; cursor: pointer; 
		.tab-button.active  background-color: white; border-bottom: 2px solid blue; 
	

imba.mount <Dashboard>
