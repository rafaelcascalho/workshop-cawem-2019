#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char** argv)
{
    float num1, num2, result;
    char op;
    char* op_string = malloc(5 * sizeof(char));
    
    printf("Entre com os dois valores separados por espaco: ");
    scanf("%f %f", &num1, &num2);

    printf("Entre com a operacao (som, sub, mult, div): ");
    scanf("%s", op_string);

    if (!strcmp(op_string, "sum")){
      result = num1 + num2;
      op = '+';
    } 
    else if(!strcmp(op_string, "sub")){
      result = num1 - num2;
      op = '-';
    }
    else if(!strcmp(op_string, "mult")){
      result = num1 * num2;
      op = 'x';
    }
    else if (!strcmp(op_string, "div")){
      result = num1 / num2;
      op = '/';
    } else{
      printf("Sua operação não foi identificada.\n");
      exit(-1);
    }
    
    printf("%.2f %c %.2f = %.2f\n", num1, op, num2, result);    
}
