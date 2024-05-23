const API_EXECUTOR_URL = 'http://127.0.0.1:8000/api/executor/';
const API_REPORT_URL = 'http://127.0.0.1:8000/api/maintenancereport/';
const API_EXECUTOR_REPORT_URL = 'http://127.0.0.1:8000/api/executorreport/';
const API_EXECUTOR_REPORT_WITH_DATA_URL = 'http://127.0.0.1:8000/api/executorreports/';

async function loadData(api_name) {
    try {
        const executorData = await fetchData(api_name);
        createArray(executorData);
        console.log(executors);

        const executorReportData = await fetchData(API_EXECUTOR_REPORT_URL);
        executorReportData.map(transformData);
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

async function fetchData(url) {
    try {
        let response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

async function fetchReports() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/maintenancereports/');
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        createCards(data);
    } catch (error) {
        console.error('Erro ao obter dados da API:', error);
    }
}

function createCards(data) {
    const statusContainers = {
        1: document.getElementById('div-created'),
        2: document.getElementById('div-assigned'),
        3: document.getElementById('div-completed')
    };

    data.forEach(item => {
        const card = createCardElement(item);
        statusContainers[item.status].appendChild(card);
    });
}

function createCardElement(item) {
    const card = document.createElement('div');
    card.className = 'card';

    const elements = [
        createElementWithText('div', 'card-id', `# ${item.id}`),
        createElementWithText('div', 'card-title', item.title),
        createElementWithText('div', 'card-date', `Date: ${item.date}`),
        createElementWithText('div', 'card-time', `Time: ${item.time_spend} min`),
        createElementWithHTML('div', 'card-button', `<a class="button-describe" onclick="loadDescribe(${item.id})">Details</a>`)
    ];

    elements.forEach(element => card.appendChild(element));
    return card;
}

function createElementWithText(tag, className, text) {
    const element = document.createElement(tag);
    element.className = className;
    element.textContent = text;
    return element;
}

function createElementWithHTML(tag, className, html) {
    const element = document.createElement(tag);
    element.className = className;
    element.innerHTML = html;
    return element;
}

function loadDescribe(id) {
    localStorage.setItem('id', id);
    window.location.href = "details.html";
}

async function exportDataToCSV() {
    try {
        const responseExecutorReport = await fetch('http://127.0.0.1:8000/api/maintenancereports/');
        if (!responseExecutorReport.ok) throw new Error('Network response was not ok');
        const jsonDataExecutorReport = await responseExecutorReport.json();

        const transformedData = jsonDataExecutorReport.map(transformData);
        const csvData = convertJSONToCSV(transformedData);

        downloadCSV(csvData, 'report_machines.csv');
    } catch (error) {
        console.error('Error fetching or processing data:', error);
    }
}

function transformData(item) {
    const shifts = { 'M': 'Morning', 'A': 'Afternoon', 'N': 'Night' };
    const statuses = { '1': 'Open', '2': 'Check', '3': 'Closed' };
    const codes = { '1': 'Code 1', '2': 'Code 2' };

    return {
        ...item,
        shift: shifts[item.shift] || item.shift,
        status: statuses[item.status] || item.status,
        code: codes[item.code] || item.code,
        executors: item.executors.map(executor => executor.name)
    };
}

function convertJSONToCSV(jsonData) {
    const headers = Object.keys(jsonData[0]);
    const csvRows = [headers.join(',')];

    jsonData.forEach(row => {
        const values = headers.map(header => `"${('' + row[header]).replace(/"/g, '\\"')}"`);
        csvRows.push(values.join(','));
    });

    return csvRows.join('\n');
}

function downloadCSV(csvData, filename) {
    const blob = new Blob([csvData], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = filename;

    document.body.appendChild(a);
    a.click();

    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}
