SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS nome_funcionario,
    d.department_name AS departamento,
    j.job_title AS cargo,
    e.salary AS salario,
    j.min_salary AS salario_minimo_cargo,
    j.max_salary AS salario_maximo_cargo
FROM HR.employees e
LEFT JOIN HR.departments d
    ON e.department_id = d.department_id
LEFT JOIN HR.jobs j
    ON e.job_id = j.job_id
WHERE e.salary >= 10000
ORDER BY e.salary DESC;