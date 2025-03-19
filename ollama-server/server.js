// Importa o framework Express para criar o servidor web
const express = require("express");

// Importa a função 'spawn' do módulo 'child_process' para executar processos do sistema operacional
const { spawn } = require("child_process");

// Cria uma instância do Express para gerenciar as rotas do servidor
const app = express();

// Define a porta na qual o servidor irá rodar
const PORT = 3000;

// =======================================================
// 1️⃣ Iniciando o Processo do Ollama
// =======================================================

// Executa o comando 'ollama serve' como um processo separado
const ollamaProcess = spawn("ollama", ["serve"]);

// Captura e exibe as saídas padrão do Ollama no terminal
ollamaProcess.stdout.on("data", (data) => {
  console.log(`Ollama: ${data}`);
});

// Captura e exibe mensagens de erro do Ollama no terminal
ollamaProcess.stderr.on("data", (data) => {
  console.error(`Ollama Error: ${data}`);
});

// Quando o processo do Ollama for encerrado, exibe uma mensagem no terminal
ollamaProcess.on("close", (code) => {
  console.log(`Ollama process exited with code ${code}`);
});

// =======================================================
// 2️⃣ Criando uma Rota para Verificar o Status do Ollama
// =======================================================

// Define uma rota GET '/status' para verificar se o Ollama está rodando
app.get("/status", (req, res) => {
  // Retorna um JSON informando que o Ollama está ativo
  res.json({ status: "Ollama is running" });
});

// =======================================================
// 3️⃣ Iniciando o Servidor Express
// =======================================================

// Faz o servidor Express escutar a porta definida
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
