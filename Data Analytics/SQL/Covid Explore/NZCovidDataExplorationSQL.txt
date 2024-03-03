SELECT *
FROM Covid19Infomation.dbo.CovidDeaths
where continent is not null
ORDER by 3,4


SELECT *
FROM Covid19Infomation.dbo.CovidVaccination
ORDER by 3,4


SELECT Location, date, total_cases, new_cases, total_deaths, population
from Covid19Infomation.dbo.CovidDeaths
ORDER by 1,2

-- Loking at Total Cases vs Total Deaths
--shows likelihood of dying if you contract covid in New Zealand
Select Location, date, total_cases, total_deaths, (cast(total_deaths as float)/cast(total_cases as float))*100.0 as DeathPercentage
from Covid19Infomation..CovidDeaths
Where location like '%Zealand%'
ORDER by 1,2

-- Loking at Total Cases vs Population
-- shows percentage of population contracted covid in New Zealand
Select Location, date, total_cases, population, (cast(total_cases as float)/cast(population as float))*100.0 as PercentOfpopulationInfected
from Covid19Infomation..CovidDeaths
Where location like '%Zealand%'
ORDER by 1,2


-- looking at countries with highedt infection rate compared to population
Select Location, MAX(total_cases) as HighestInfrectionCount, population, (cast(MAX(total_cases) as float)/cast(population as float))*100.0 as PercentPopulationInfected
from Covid19Infomation..CovidDeaths
Group by Location, population
ORDER by PercentPopulationInfected desc

-- Showing Countries with the Highest deathout per population

Select Location, MAX(cast(total_deaths as float)) as TotalDeathCount, population, (cast(MAX(total_deaths) as float)/cast(population as float))*100.0 as PercentPopulationdeaths
from Covid19Infomation..CovidDeaths
where continent is not null
Group by Location, population
ORDER by PercentPopulationdeaths desc

--Showing highest death count by Continent

Select continent, MAX(cast(total_deaths as float)) as TotalDeathCount
from Covid19Infomation..CovidDeaths
where continent is not null
Group by continent
ORDER by TotalDeathCount desc

-- Global numbers

Select SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as float)) / SUM(cast(New_Cases AS float))*100 as DeathPercentage
From Covid19Infomation..CovidDeaths
where continent is not null 
order by 1,2

--looking at total population vs vaccinations

with PopvsVac (continent, location, date, population, RollingVaccinated, new_vaccinations)
as
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, SUM(CONVERT(float, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.date) as RollingVaccinated
From Covid19Infomation..CovidDeaths dea
join Covid19Infomation..CovidVaccination vac
	on dea.location = vac.location
	and dea.date = VAC.date
	where dea.continent is not null
	--order by 2,3
	)
	Select *, (cast(RollingVaccinated AS float)/cast(population as float))*100 as vaccinationPercentage
	From PopvsVac

	-- as Temp Table
DROP Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
continent nvarchar (225)
, location nvarchar (225)
, date datetime
, population numeric
, new_vaccinations numeric
, RollingVaccinated numeric
)
Insert into #PercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, SUM(CONVERT(float, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.date) as RollingVaccinated
From Covid19Infomation..CovidDeaths dea
join Covid19Infomation..CovidVaccination vac
	on dea.location = vac.location
	and dea.date = VAC.date
	where dea.continent is not null
	--order by 2,3
	Select *, (RollingVaccinated/population)*100 as vaccinationPercentage
	From #PercentPopulationVaccinated

	-- Creating view to store data for later visualizations

 Create View PercentPopulationVaccinated as 

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, SUM(CONVERT(float, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.date) as RollingVaccinated
From Covid19Infomation..CovidDeaths dea
join Covid19Infomation..CovidVaccination vac
	on dea.location = vac.location
	and dea.date = VAC.date
	where dea.continent is not null
	--order by 2,3
