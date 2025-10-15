/* ======================================================
   SCRIPT.JS — LÓGICA DA PÁGINA E CHAMADA HTTP
   ====================================================== */

/* 1. Seleciona elementos e define variáveis globais */
const API_URL = 'https://jsonplaceholder.typicode.com/users'; // API de teste pública
const btnRefresh = document.getElementById('btnRefresh');
const btnClear = document.getElementById('btnClear');
const output = document.getElementById('output');
const status = document.getElementById('status');
const miniSpinner = document.getElementById('miniSpinner');
const miniText = document.getElementById('miniText');
const lastUpdate = document.getElementById('lastUpdate');
const emptyMessage = document.getElementById('emptyMessage');

/* ======================================================
   2. Função principal — FAZ A REQUISIÇÃO HTTP
   ====================================================== */
function fetchClients() {
    // Atualiza a interface para mostrar que está carregando
    setStatus('Carregando clientes...', true);

    // Cria o objeto XMLHttpRequest (igual ao exemplo da imagem)
    const xhttp = new XMLHttpRequest();

    // Função que será executada cada vez que o estado da requisição mudar
    xhttp.onreadystatechange = function () {
        // Quando readyState = 4 significa que a resposta chegou
        if (this.readyState === 4) {
            // Atualiza o status para "Pronto" (independente do resultado)
            setStatus('Pronto', false);

            // Verifica se o status HTTP foi 200 (OK)
            if (this.status === 200) {
                try {
                    // Converte o texto recebido (JSON) em objeto JavaScript
                    const data = JSON.parse(this.responseText);
                    // Mostra os dados em formato de tabela
                    renderTable(data);
                    // Atualiza data/hora da última atualização
                    lastUpdate.textContent = new Date().toLocaleString();
                } catch (err) {
                    // Caso o JSON seja inválido
                    renderError('Resposta inválida do servidor.');
                }
            } else {
                // Caso o status seja diferente de 200 (ex: 404 ou 500)
                renderError('Erro na requisição. Código: ' + this.status);
            }
        }
    };

    // Caso aconteça algum erro de rede (sem internet, etc.)
    xhttp.onerror = function () {
        setStatus('Erro', false);
        renderError('Falha na conexão (erro de rede).');
    };

    // Caso demore muito e ultrapasse o tempo limite
    xhttp.ontimeout = function () {
        setStatus('Erro', false);
        renderError('Tempo de espera esgotado (timeout).');
    };

    // Abre a conexão HTTP: método GET, endereço da API e modo assíncrono
    xhttp.open('GET', API_URL, true);

    // Define um tempo máximo de espera de 7 segundos
    xhttp.timeout = 7000;

    // Envia a requisição para o servidor
    xhttp.send();
}

/* ======================================================
   3. Funções auxiliares de interface
   ====================================================== */

// Atualiza o texto e o spinner de status
function setStatus(text, loading) {
    status.innerHTML = loading
        ? '<div class="spinner"></div><span style="margin-left:8px;color:var(--muted)">' + text + '</span>'
        : '<span class="muted">' + text + '</span>';

    miniSpinner.style.display = loading ? 'inline-block' : 'none';
    miniText.style.opacity = loading ? '0.6' : '1';

    if (!loading) {
        miniText.textContent = 'Última atualização: ' + (lastUpdate.textContent || '—');
    }
}

// Cria uma tabela HTML com os dados recebidos
function renderTable(users) {
    if (!Array.isArray(users) || users.length === 0) {
        output.innerHTML = '<div class="empty">Nenhum cliente encontrado.</div>';
        return;
    }

    // Monta o HTML da tabela linha por linha
    let html = '<table><thead><tr><th>Nome</th><th>Email</th><th>Empresa</th><th>Telefone</th></tr></thead><tbody>';
    users.forEach(u => {
        const name = String(u.name || '');
        const email = String(u.email || '');
        const company = (u.company && u.company.name) ? String(u.company.name) : '';
        const phone = String(u.phone || '');
        html += `
      <tr>
        <td data-label="Nome">${escapeHtml(name)}</td>
        <td data-label="Email">${escapeHtml(email)}</td>
        <td data-label="Empresa">${escapeHtml(company)}</td>
        <td data-label="Telefone">${escapeHtml(phone)}</td>
      </tr>`;
    });
    html += '</tbody></table>';

    // Exibe o conteúdo montado na área de output
    output.innerHTML = html;
    emptyMessage.style.display = 'none';
}

// Exibe mensagem de erro na tela
function renderError(message) {
    output.innerHTML = `<div class="error card" style="padding:12px;border-radius:8px">${escapeHtml(message)}</div>`;
}

// Evita injeção de HTML (segurança básica)
function escapeHtml(s) {
    return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

// Limpa o conteúdo exibido
function clearOutput() {
    output.innerHTML = '<div class="empty" id="emptyMessage">Clique em "Atualizar lista" para buscar clientes.</div>';
    lastUpdate.textContent = '—';
}

/* ======================================================
   4. Eventos dos botões
   ====================================================== */

// Quando o usuário clica em "Atualizar lista"
btnRefresh.addEventListener('click', function () {
    fetchClients();
});

// Quando o usuário clica em "Limpar"
btnClear.addEventListener('click', function () {
    clearOutput();
});
