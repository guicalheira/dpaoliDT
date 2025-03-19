global css body c:black bg:#F5F5F5 ff:Arial inset:0 d:vcc bg:white h:100vh box-sizing:border-box m:0 p:0 ff:"Inter", sans-serif fs:14px c:#333

tag Dashboard

	activeTab = "rotinas"
	
	def switchTab(tab)
		activeTab = tab
	
	<self>
		
		css 
			w:100% 
			h:100%
			d:grid 
			gtc:100px 1fr 1fr 1fr 1fr  
			gtr:70px 60px 1fr 1fr 1fr
			gcg:0px 
			grg:0px 
			gta:"header header header header header""sidebar midbar midbar midbar midbar""sidebar main main second second""sidebar main main second second" "sidebar main main second second" 
			bg:#F5F5F5 
			
		
	
		<.header>
			css 
				grid-area:header 
				d:flex 
				ai:center 
				jc:space-between 
				h:70px 
				px:20 
				bg:white
				bs:0 2px 8px rgba(0,0,0,0.1) 
				bbe:1px solid #E5E7EB
			<.left>
				css d:flex ai:center 
 
			<h2> "Dominio"
			 
			<.right>
				css d:flex ai:center g:5px 
			<a href="#"> "Playground"
			<a href="#"> "Dashboard"
			<a href="#"> "Docs"
			<a href="#"> "API reference"
			
			<.profile>
				css w:32px h:43px rd:50% bg:#ccc
       	 	
		
		<.midbar>
			css 
				grid-area: midbar 
				bg:green 
				   
				grid-area: midbar 
				d:flex 
				ai:center 
				jc:space-between
				h:100%
				px:16px 
				bg:#F5F5F5
				bbe:1px solid #E5E7EB
			<.left>
			css d:flex ai:center g:8px
			<a href="#"> "← Logs"
			<.right>
			css d:flex ai:center g:16px
			<button.icon>
				css d:flex ai:center g:4px bg:transparent border:none cursor:pointer
				"🔄"
					

		<.sidebar>
			css w:100% h:100% bg:#F5F5F5 c:black  d:flex fld:column ai:center grid-area:sidebar   
			<h2> "Eventos"
			
			<.events>
			css flex:1 oy:auto  
			<.event-item  @click=switchTab("logs").activeTab =("logs" ? "active" : "")> "Logs"
			<.event-item  @click=switchTab("rotinas").activeTab =("rotinas" ? "active" : "")> "Rotinas"
			
			
		
		
			
		<.request-box>
			css bg:white sh:0 2px 4px rgba(0,0,0,0.1) rd:5 p:4 mb:4 grid-area: second   h:fit-content 
			<h3> "Janela Interativa de Requisições"
			<textarea rows=3 placeholder="Digite a solicitação...">
			<.button-textArea>
			<button> "Enviar"
			
		<.tabs>
			css d:flex fld:column  mb:3 g:10px  grid-area: main   h:100%
		
			
			if activeTab == "rotinas"
				<.tab-content>
					css bg:white p:3 sh:0 2px 4px rgba(0,0,0,0.1) rd:5 c:black  h:100%
					<h3> "Rotinas"
					<ul>
						<li> "Execução de Cadastro"
						<li> "Monitoramento de Arquivos"
						<li> "Verificação de Logs"
			
			if activeTab == "logs"
				<.tab-content>
					css bg:white p:3 sh:0 2px 4px rgba(0,0,0,0.1) rd:5 c:black   h:100%
					<h3> "Logs"
					<p> "[12:00] Processando requisição..."
					<p> "[12:01] Arquivo localizado"
					<p> "[12:02] Dados extraídos"
 
	
	css
		.sidebar h2  fw:bold fs:1.4em mb:2  
		.event-item   bg:#EAEAEA p:8px mb:5px br:6px shadow-sm transition:0.3s cursor:default
		.event-item@hover  bg:#D8D8D8 
		.tab-button   p:10px border:1px solid #ccc cursor:pointer bg:#f1f5f9 rd:5 transition:0.2s
		.tab-button@hover  bg:white  
		.log-entry padding: 8px border-bottom: 1px solid #ddd transition: background 0.2s
		.request-box button  bg:#4A90E2 c:white fw:bold p:10px br:6px border:none transition:0.3s cursor:pointer
		.request-box button@hover bg:#357ABD 
		.request-box textarea w:500px h:80px p:8px br:6px border:1px solid #CCC bg:#F9F9F9 resize:none 
		.header a td:none c:#555 fw:500 fs:14px transition: color 0.3s ease
		.header a@hover c:black td:underline
		.profile w:36px h:36px rd:50% bg:#ccc
		.header h2 fs:1.8em fw:bold c:#333 
		
		
		.sidebar  bd: 1px solid #E5E7EB  bs: 2px 0px 4px rgba(0, 0, 0, 0.05)  
		.request-box  bd: 1px solid #E5E7EB  bs: 0px 2px 4px rgba(0, 0, 0, 0.1)  
		.tabs  bd: 1px solid #E5E7EB  bs: 0px 2px 4px rgba(0, 0, 0, 0.1)  
		.midbar  bs: 0px 2px 4px rgba(0, 0, 0, 0.1)  bd: 1px solid #E5E7EB
	

imba.mount <Dashboard>