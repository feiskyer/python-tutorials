#!/usr/bin/env python

def merge(a, start, m, end):
	temp=[]
	sum=0
	#a=[]
	#a.extend(arr)
	i,j=start,m+1
	while i<=m and j<=end:
		if a[i]>a[j]:
			temp.append(a[j])
			j+=1
			sum += m-i+1
		else:
			temp.append(a[i])
			i+=1
	while i<=m: 
		temp.append(a[i])
		i+=1
	while j<=end: 
		temp.append(a[j])
		j+=1
	
	i=0
	while i< len(temp):
		arr[start+i]=temp[i]
		i+=1

	return sum

def merger_sort(arr, start, end):
	ret=0
	m=0
	if start < end:
		m=(start+end)/2
		ret+=merger_sort(arr, start, m)
		ret+=merger_sort(arr, m+1, end)
		ret+=merge(arr, start, m, end)

	return ret


T=int(raw_input())

for i in xrange(T):
	n=int(raw_input())
	arr_in=raw_input()
	array=arr_in.split(' ')
	arr=[int(elem) for elem in array]
	print merger_sort(arr, 0, n-1)
