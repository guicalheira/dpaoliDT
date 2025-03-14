global css body c:black bg:warm8 ff:Arial inset:0 d:vcc bg:white h:100vh box-sizing:border-box m:0 p:0

tag Dashboard

	activeTab = "rotinas"
	
	def switchTab(tab)
		activeTab = tab
	
	<self>
		
		css 
			w:100% 
			h:100vh
			d:grid 
			gtc:repeat(5, 1fr) 
			gtr:70px 60px 1fr 1fr 1fr
			gcg:0px 
			grg:0px 
			gta:"header header header header header""sidebar midbar midbar midbar midbar""sidebar main main second second""sidebar main main second second" "sidebar main main second second"   
			bg:#F5F5F5 
			
		
	
		<.header>
			css grid-area: header bg:blue bd: 1px solid gray  
			<h1> "HEADER"
		<.header>
			css grid-area: midbar bg:green bd: 1px solid gray  
			<h1> "MIDBAR"	

		<.sidebar>
			css w:fit-content h:100% bg:#1e293b c:white px:4 d:flex fld:column grid-area: sidebar  bd: 1px solid gray  
			<h2> "Eventos"
			
			
			<.events>
				css flex:1 oy:auto
				
				<p.event-item> "[12:00] Nova requisição processada"
				<p.event-item> "[12:05] Erro em arquivo X"
				<p.event-item> "[12:10] Cadastro de cliente concluído"
		
		
			
		<.request-box>
			css bg:white sh:0 2px 4px rgba(0,0,0,0.1) rd:5 p:4 mb:4 grid-area: second bd: 1px solid gray  
			<h3> "Janela Interativa de Requisições"
			<textarea rows=3 placeholder="Digite a solicitação..."><textarea>
			<button> "Enviar"
			
		<.tabs>
			css d:flex fld:column  mb:3 g:10px  grid-area: main bd: 1px solid gray  
			<.buttons>
				css p:10px b:1px solid #ccc cursor:pointer bg:#f1f5f9 c:black d:flex g:1
				<button.tab-button @click=switchTab("rotinas").activeTab =("rotinas" ? "active" : "")> "Rotinas"
				<button.tab-button @click=switchTab("logs").activeTab =("logs" ? "active" : "")> "Logs"
			
			if activeTab == "rotinas"
				<.tab-content>
					css bg:white p:3 sh:0 2px 4px rgba(0,0,0,0.1) rd:5 c:black
					<h3> "Rotinas"
					<ul>
						<li> "Execução de Cadastro"
						<li> "Monitoramento de Arquivos"
						<li> "Verificação de Logs"
			
			if activeTab == "logs"
				<.tab-content>
					css bg:white p:3 sh:0 2px 4px rgba(0,0,0,0.1) rd:5 c:black
					<h3> "Logs"
					<p> "[12:00] Processando requisição..."
					<p> "[12:01] Arquivo localizado"
					<p> "[12:02] Dados extraídos"
 
	
	css
		.sidebar h2  fw:bold fs:1.4em mb:2  
		.event-item  bg:#334155 p:2 rd:3 mb:2 
		.tab-button  p:10px b:1px solid #ccc cursor:pointer bg:#f1f5f9 c:black
		.tab-button.active  bg:white bb:2px solid blue fw:bold
		.request-box button  bg:#3b82f6 c:white p:10px rd:3 b:none cursor:pointer mt:2
		button@hover  bg:#2563eb bc:#2563eb
	

imba.mount <Dashboard>