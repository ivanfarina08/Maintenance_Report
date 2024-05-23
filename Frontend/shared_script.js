const API_EXECUTOR_URL = 'http://127.0.0.1:8000/api/executor/';
const API_REPORT_URL = 'http://127.0.0.1:8000/api/maintenancereport/';
const API_EXECUTOR_REPORT_URL = 'http://127.0.0.1:8000/api/executorreport/';
const API_EXECUTOR_REPORT_WITH_DATA_URL = 'http://127.0.0.1:8000/api/executorreports/';

async function api_name(name) {
    switch (name) {
        case 'executor':
            return API_EXECUTOR_URL;
        case 'report':
            return API_REPORT_URL;
        case 'executor_report':
            return API_EXECUTOR_REPORT_URL;
        case 'executor_report_with_data':
            return API_EXECUTOR_REPORT_WITH_DATA_URL;
        default:
            throw new Error(`Unknown API name: ${name}`);
    }
}

async function loadData(url) {
    try {
        return await fetchData(url);        
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
    }
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


async function sendRequest(url, method, data) {
    const response = await fetch(url, {
        method: method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
    }

    return response.json();
}