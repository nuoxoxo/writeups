#include "iostream"
using	namespace std;
int main(){
	const char *s = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}";
	string	res;
	int	c, i = -1;
	while (s[++i]) {
		c = s[i];
		if (c <= 'z' && c >= 'a') {
			c += 13;
			if (c > 'z')
				c = c - 'z' + 'a' - 1;
		} else if (c <= 'Z' && c >= 'A') {
			c -= 13;
			if (c < 'A')
				c = 'Z' - 'A' + c + 1;
		}
		cout << (char) c;
		res += c;
	}
	assert(res == "picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}");
}
