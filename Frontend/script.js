getDataFromAPI();
function checkCodeInterlock() {
    const code1 = document.getElementById('code1');
    const code2 = document.getElementById('code2');

    if (code1.checked) {
        code2.checked = false;
    } else if (code2.checked) {
        code1.checked = false;
    }
}

function submitForm() {
    event.preventDefault();

    const date = document.getElementById('date').value;
    const shift = document.getElementById('shift').value;
    const lineMachine = document.getElementById('lineMachine').value;
    const code1 = document.getElementById('code1').checked ? 'Yes' : 'No';
    const code2 = document.getElementById('code2').checked ? 'Yes' : 'No';
    const faultDescription = document.getElementById('faultDescription').value;
    const numberOfPeople = document.getElementById('numberOfPeople').value;
    const timeSpent = document.getElementById('timeSpent').value;

    if (!date || !shift || !lineMachine || !(code1 || code2) || !faultDescription || !numberOfPeople || !timeSpent) {
        alert('Please fill in all fields and select one of the checkboxes.');
        return;
    }

    const table = document.getElementById('reportTable');
    const tbody = document.getElementById('reportTableBody');
    const newRow = tbody.insertRow();

    newRow.innerHTML = `
                <td>${date}</td>
                <td>${shift}</td>
                <td>${lineMachine}</td>
                <td>${code1}</td>
                <td>${code2}</td>
                <td>${faultDescription}</td>
                <td>${numberOfPeople}</td>
                <td>${timeSpent}</td>
            `;

    document.getElementById('reportForm').reset();

    document.getElementById('downloadButton').style.display = 'block';
}

function confirmReset() {
    const confirmBox = confirm('Have you already downloaded the data? Resetting will clear all data.');

    if (confirmBox) {
        downloadReport();
        resetForm();
    }
}

function resetForm() {
    document.getElementById('reportForm').reset();
    document.getElementById('reportTableBody').innerHTML = '';
    document.getElementById('downloadButton').style.display = 'none';
}

function downloadReport() {
    const table = document.getElementById('reportTable');

    const exportTable = document.createElement('table');
    exportTable.innerHTML = table.innerHTML;

    const tempHTML = document.createElement('html');
    tempHTML.appendChild(exportTable);

    const excelContent =
        `<html xmlns:x="urn:schemas-microsoft-com:office:excel">
                <head>
                    <!--[if gte mso 9]>
                    <xml>
                        <x:ExcelWorkbook>
                            <x:ExcelWorksheets>
                                <x:ExcelWorksheet>
                                    <x:Name>Report</x:Name>
                                    <x:WorksheetOptions>
                                        <x:DisplayGridlines/>
                                    </x:WorksheetOptions>
                                </x:ExcelWorksheet>
                            </x:ExcelWorksheets>
                        </x:ExcelWorkbook>
                    </xml>
                    <![endif]-->
                </head>
                <body>
                    ${tempHTML.innerHTML}
                </body>
                </html>`;

    const blob = new Blob([excelContent], { type: 'application/vnd.ms-excel' });
    const url = URL.createObjectURL(blob);

    const downloadLink = document.createElement('a');
    downloadLink.href = url;
    downloadLink.download = 'maintenance_report.xls';
    downloadLink.click();

    URL.revokeObjectURL(url);
}