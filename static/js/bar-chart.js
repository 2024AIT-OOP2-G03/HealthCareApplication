// HTMLで渡されたPythonのデータを利用
const sleeptime = sleepData.map(item => item.sleeptime); // 睡眠時間
const date = sleepData.map(item => item.date);   // 月日

// 棒グラフを描画
const ctx = document.getElementById('barChart').getContext('2d');
const barChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: date,
        datasets: [{
            label: '睡眠時間 (時間)',
            data: sleeptime,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
