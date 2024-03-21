NAME = ft_gomoku_ai

SRCS = grid/grid.cpp \
		tools/nex_gen.cpp \
		run_ai.cpp \
		priority.cpp \
		matching_cases.cpp \

OBJS = ${SRCS:.cpp=.o}

FLAGS = -Wall -Wextra -Werror -g3 -fPIC

CC = g++

.cpp.o:
	${CC} ${FLAGS} -c $< -o ${<:.cpp=.o}

all : $(NAME)

$(NAME): ${OBJS}
	${CC} ${FLAGS} ${OBJS} -o ${NAME}


lib:
	${CC} -shared -o ${NAME}.so ${OBJS}

clean:
	rm -rf ${OBJS}

fclean: clean
	rm -rf ${NAME}

re: fclean all

.PHONY: re all clean fclean lib
