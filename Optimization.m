billing_dates = optimvar('billing_dates', 3, 1, 'Type', 'integer', 'LowerBound', 1, 'UpperBound', 30);
max_cycle_times = [55; 48; 47];
f = fcn2optimexpr(@totalmonthlycycletime, billing_dates, max_cycle_times, "OutputSize", [1, 1], "Display","on");
f = - f;
prob = optimproblem('Objective', f);
show(prob)
x0.billing_dates = [10; 26; 27];
tic
[sol, fval, exitflag, output] = solve(prob, x0);
toc
disp(sol.billing_dates)
fval = 0 - fval;
disp(fval)
disp(exitflag)