# COVID Data Exploration SQL
Exploration of COVID-19 data for New Zealand using SQL. The project utilizes data from the World Health Organization to analyze and explore trends in COVID-19 data specific to New Zealand.

This SQL project involves a comprehensive exploration of COVID-19 data, inspired by the insightful YouTube tutorial series by [AlexTheAnalyst](https://www.youtube.com/watch?v=qfyynHBFOsM&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF&index=19) and referencing data from [Our World in Data](https://ourworldindata.org/covid-deaths).

# SQL Scripts

## 1. COVID Deaths Analysis

Filtered by Continent

SELECT *

FROM Covid19Infomation.dbo.CovidDeaths

WHERE continent IS NOT NULL

ORDER BY continent, date;

### Filtered by Location

SELECT *

FROM Covid19Infomation.dbo.CovidDeaths

ORDER BY Location, date;

### Total Cases vs Total Deaths in New Zealand

SELECT Location, date, total_cases, total_deaths, (CAST(total_deaths AS float) / CAST(total_cases AS float)) * 100.0 AS DeathPercentage

FROM Covid19Infomation.dbo.CovidDeaths

WHERE Location LIKE '%Zealand%'

ORDER BY Location, date;

### Total Cases vs Population in New Zealand

SELECT Location, date, total_cases, population, (CAST(total_cases AS float) / CAST(population AS float)) * 100.0 AS PercentOfPopulationInfected

FROM Covid19Infomation.dbo.CovidDeaths

WHERE Location LIKE '%Zealand%'

ORDER BY Location, date;

### Countries with Highest Infection Rate

SELECT Location, MAX(total_cases) AS HighestInfectionCount, population, (CAST(MAX(total_cases) AS float) / CAST(population AS float)) * 100.0 AS PercentPopulationInfected

FROM Covid19Infomation.dbo.CovidDeaths

GROUP BY Location, population

ORDER BY PercentPopulationInfected DESC;

### Countries with Highest Death Rate


SELECT Location, MAX(CAST(total_deaths AS float)) AS TotalDeathCount, population, (CAST(MAX(total_deaths) AS float) / CAST(population AS float)) * 100.0 AS PercentPopulationDeaths

FROM Covid19Infomation.dbo.CovidDeaths

WHERE continent IS NOT NULL

GROUP BY Location, population

ORDER BY PercentPopulationDeaths DESC;

### Highest Death Count by Continent

SELECT continent, MAX(CAST(total_deaths AS float)) AS TotalDeathCount

FROM Covid19Infomation.dbo.CovidDeaths

WHERE continent IS NOT NULL

GROUP BY continent

ORDER BY TotalDeathCount DESC;

### Global COVID Numbers

SELECT SUM(new_cases) AS total_cases, SUM(CAST(new_deaths AS int)) AS total_deaths, SUM(CAST(new_deaths AS float)) / SUM(CAST(New_Cases AS float)) * 100 AS DeathPercentage

FROM Covid19Infomation.dbo.CovidDeaths

WHERE continent IS NOT NULL;

## 2. Population vs Vaccinations

### Rolling Vaccination Percentage

WITH PopvsVac (continent, location, date, population, RollingVaccinated, new_vaccinations)

AS

(
	SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, SUM(CONVERT(float, vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.date) AS RollingVaccinated
	FROM Covid19Infomation.dbo.CovidDeaths dea
	JOIN Covid19Infomation.dbo.CovidVaccination vac
		ON dea.location = vac.location
		AND dea.date = VAC.date
	WHERE dea.continent IS NOT NULL
)

SELECT *, (CAST(RollingVaccinated AS float) / CAST(population AS float)) * 100 AS VaccinationPercentage

FROM PopvsVac;

##Temporary Table: Population vs Vaccinations

DROP TABLE IF EXISTS #PercentPopulationVaccinated;

CREATE TABLE #PercentPopulationVaccinated

(
	continent NVARCHAR(225),
	location NVARCHAR(225),
	date DATETIME,
	population NUMERIC,
	new_vaccinations NUMERIC,
	RollingVaccinated NUMERIC
);

INSERT INTO #PercentPopulationVaccinated

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, SUM(CONVERT(float, vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.date) AS RollingVaccinated

FROM Covid19Infomation.dbo.CovidDeaths dea

JOIN Covid19Infomation.dbo.CovidVaccination vac
	ON dea.location = vac.location
	AND dea.date = VAC.date
 
WHERE dea.continent IS NOT NULL;

SELECT *, (RollingVaccinated / population) * 100 AS VaccinationPercentage

FROM #PercentPopulationVaccinated;

### View: Population vs Vaccinations

CREATE VIEW PercentPopulationVaccinated AS

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, SUM(CONVERT(float, vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.date) AS RollingVaccinated

FROM Covid19Infomation.dbo.CovidDeaths dea

JOIN Covid19Infomation.dbo.CovidVaccination vac
	ON dea.location = vac.location
	AND dea.date = VAC.date
 
WHERE dea.continent IS NOT NULL;

Usage

Clone the repository and explore the SQL scripts to conduct an in-depth analysis and exploration of COVID-19 data.
