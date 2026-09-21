SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS nome_funcionario,
    e.salary AS salario,
    d.department_name AS departamento,
    l.city AS cidade,
    l.state_province AS estado,
    c.country_name AS pais,
    r.region_name AS regiao
FROM HR.employees e
LEFT JOIN HR.departments d
    ON e.department_id = d.department_id
LEFT JOIN HR.locations l
    ON d.location_id = l.location_id
LEFT JOIN HR.countries c
    ON l.country_id = c.country_id
LEFT JOIN HR.regions r
    ON c.region_id = r.region_id
WHERE e.salary > 0
ORDER BY r.region_name, c.country_name, l.city, e.salary DESC;