async function loadPopulationData() {

  try {

    const response = await fetch(
  "./data/cleaned.json?v=20260914",
  { cache: "no-store" }
);

    if (!response.ok) {
      throw new Error(
        "Population data could not be loaded"
      );
    }

    const data = await response.json();

    showPopulationCards(data.records);
    showSummary(data.summary);
    drawChart(data.records);

  } catch (error) {

    console.error(error);

    document
      .getElementById("populationChart")
      .innerHTML =
      "<p>Population data failed to load.</p>";
  }
}


function showPopulationCards(records) {

  records.forEach(item => {

    const element =
      document.getElementById(
        `pop${item.year}`
      );

    if (element) {

      const billions =
        item.population_millions / 1000;

      element.textContent =
        billions.toFixed(2);
    }

  });
}


function showSummary(summary) {

  document
    .getElementById("average")
    .textContent =
    (
      summary.average_population_millions
      / 1000
    ).toFixed(2)
    + " billion";


  document
    .getElementById("growth")
    .textContent =
    summary
      .growth_rate_2024_2100_percent
    + "%";


  document
    .getElementById("cagr")
    .textContent =
    summary.cagr_2024_2100_percent
    + "% / year";
}


function drawChart(records) {

  const chart =
    document.getElementById(
      "populationChart"
    );

  chart.innerHTML = "";


  const maxPopulation =
    Math.max(
      ...records.map(
        item =>
          item.population_millions
      )
    );


  records.forEach(item => {

    const group =
      document.createElement("div");

    group.className = "bar-group";


    const value =
      document.createElement("div");

    value.className = "bar-value";

    value.textContent =
      (
        item.population_millions
        / 1000
      ).toFixed(2)
      + "B";


    const bar =
      document.createElement("div");

    bar.className = "bar";

    const percentage =
      (
        item.population_millions
        / maxPopulation
      ) * 100;

    bar.style.height =
      percentage + "%";


    const label =
      document.createElement("div");

    label.className =
      "bar-label";

    label.textContent =
      item.year;


    group.appendChild(value);
    group.appendChild(bar);
    group.appendChild(label);

    chart.appendChild(group);

  });
}


loadPopulationData();
