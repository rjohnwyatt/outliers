pro derbyalt_ten_skaters, factor, num
; where factor is the number of std deviations to define which points to toss, and num is the number of skaters on the team I'm running

keep_sd=dblarr(num) --creates an array with num values - JW
keep_ave=dblarr(num) --creates an array with num values - JW
keep_med=dblarr(num) --creates an array with num values - JW

for i=0,num-1 do begin --runs through all the skater ranking files

p=i+1
readcol, '2012/as'+strcompress(p, /remove_all)+'.txt', v1,v2,v3,v4,v5,v6,v7,v8,v9,v10, format='f,f,f,f,f,f,f,f,f'
c=dblarr(17)	; 17 for the number of rankers this year

 for r=0,16 do begin
  c(r) = v1(r) + v2(r) + v3(r) + v4(r) + v5(r) + v6(r) + v7(r) + v8(r) + v9(r) + v10(r)
 endfor

c_high=mean(c) + factor*stddev(c) --establishes high end of range
c_low=mean(c) - factor*stddev(c) --establishes low end of range
c_w=where(c lt c_high AND c gt c_low) --lt= less than, gt = greater than, where = selects the values that meet the criteria

keep_sd(i)=mean(c(c_w)) --adds current skater's standard deviation into the array of standard deviations - JW
keep_ave(i)=mean(c) --adds current skater's means into the array of means - JW
keep_med(i)=median(c, /even) --adds current skater's medians into the array of medians - JW

print, 'AS'+strcompress(p, /remove_all)+' ', stddev(c), ' Votes discarded: ', n_elements(where(c gt c_high OR c lt c_low)), ' , Average of remaining votes: ', mean(c(c_w)), ' , Average of all votes: ', mean(c), ', (Median =)', median(c, /even)
-- prints individual data

endfor

print, 'Team averages. Average of remaining votes: ', mean(keep_sd), ' Average of all votes: ', mean(keep_ave), ' Average of median votes: ', mean(keep_med)
-- prints team data

stop
end
