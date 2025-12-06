# Make disk online
diskpart
list disk
select disk 1
online disk
exit

# Initialize disk (if initialize in gui is greyed out)
diskpart
list disk
select disk 1
attributes disk clear readonly
convert mbr
exit
