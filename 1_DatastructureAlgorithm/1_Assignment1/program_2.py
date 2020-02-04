def Replace(mStr, pat, rep):
    for i in range(len(mStr)):
        if pat == mStr[i:i+len(pat)]:
            mStr = mStr[:i] + rep + mStr[i+len(pat):]
    return mStr

main_string = input("Enter main string: ")
pat_string = input("Enter pattern string: ")
rep_string = input("Enter replace string: ")
res = Replace(main_string, pat_string, rep_string)
print(res)
