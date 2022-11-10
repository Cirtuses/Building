sum_measurecurrent = 0.51
measure_count = 5

mean_current = format(float(sum_measurecurrent)/float(measure_count), '.4f')
mean_current = float((mean_current * 1000)/1000)
print(type(mean_current), mean_current)
