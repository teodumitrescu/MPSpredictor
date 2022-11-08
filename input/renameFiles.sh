#!/bin/bash
i=0
for file in *.CSV
do
	mv "$file" "input$i.CSV"
	((i=i+1))
done
