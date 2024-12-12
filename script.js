// Get references to HTML elements
const startButton = document.getElementById('startButton');
const latencyElement = document.getElementById('latency');
const sizeElement = document.getElementById('size');
const statusElement = document.getElementById('status');
const logTableBody = document.querySelector('#logTable tbody');
const trafficPlot = document.getElementById('trafficPlot');
let plotData = { latency: [], size: [] };
let anomalyData = [];

// Initialize chart
const chart = new Chart(trafficPlot, {
  type: 'line',
  data: {
    labels: [],
    datasets: [
      {
        label: 'Latency (ms)',
        data: plotData.latency,
        borderColor: 'blue',
        fill: false,
      },
      {
        label: 'Size (bytes)',
        data: plotData.size,
        borderColor: 'green',
        fill: false,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      x: {
        title: {
          display: true,
          text: 'Traffic Instance',
        },
      },
      y: {
        title: {
          display: true,
          text: 'Value',
        },
      },
    },
  },
});

// Start button click handler
startButton.addEventListener('click', () => {
  startButton.disabled = true; // Disable button during simulation
  simulateRealTimeTraffic();
});

// Simulate real-time traffic data
function simulateRealTimeTraffic() {
  let trafficIndex = 0;

  // Simulate traffic every second
  const interval = setInterval(() => {
    trafficIndex++;

    // Randomly generate latency and size
    const latency = (Math.random() * 150 + 50).toFixed(2); // Latency between 50-200 ms
    const size = (Math.random() * 300 + 200).toFixed(2); // Size between 200-500 bytes

    // Simulate anomaly detection (50% chance of anomaly)
    const isAnomaly = Math.random() < 0.05;

    // Update the display
    latencyElement.textContent = latency;
    sizeElement.textContent = size;
    statusElement.textContent = isAnomaly ? 'Anomalous' : 'Normal';
    statusElement.style.color = isAnomaly ? 'red' : 'green';

    // Update plot data
    plotData.latency.push(latency);
    plotData.size.push(size);
    chart.data.labels.push(trafficIndex);
    chart.update();

    // Log the anomaly if detected
    if (isAnomaly) {
      const timestamp = new Date().toLocaleString();
      logAnomaly(timestamp, latency, size);
    }

    // Stop after 1 minute
    if (trafficIndex >= 60) {
      clearInterval(interval);
      startButton.disabled = false; // Enable button after simulation
    }
  }, 1000);
}

// Function to log anomalies to the table
function logAnomaly(timestamp, latency, size) {
  const row = document.createElement('tr');
  row.innerHTML = `
    <td>${timestamp}</td>
    <td>${latency} ms</td>
    <td>${size} bytes</td>
    <td>Anomalous</td>
  `;
  logTableBody.appendChild(row);
}
