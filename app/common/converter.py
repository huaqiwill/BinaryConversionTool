class NumberConverter:
    @staticmethod
    def convert(value: str, from_base: int) -> dict:
        """
        将输入值转换为各种进制
        """
        try:
            if not value.strip():
                return {}
            
            # 转换为十进制
            if from_base == 16:
                decimal_num = int(value, 16)
            else:
                decimal_num = int(value, from_base)
            
            # 返回各种进制的结果
            return {
                "二进制": bin(decimal_num)[2:],
                "八进制": oct(decimal_num)[2:],
                "十进制": str(decimal_num),
                "十六进制": hex(decimal_num)[2:].upper()
            }
        except ValueError:
            return {}