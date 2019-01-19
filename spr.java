//SCISSOR-PAPER-ROCK GAME
//Author : HUSAIN SHAIKH
//27 January 2018

import java.util.*;
public class game {
static Scanner input=new Scanner (System.in);
static Random rand=new Random();
static String name;
static int user=0;;
static String again;
static int computer=0;
	public static void main(String[] args) {
		intro();
		while(true)
		{
			for(int i=0;user<5||computer<5;i++) 
			{
				System.out.println("What do you want to choose ? ");
				String userch=input.next();
				if(userch.startsWith("s")||userch.startsWith("S"))
				{
					userch="SCISSOR";
				}
				else if(userch.startsWith("r")||userch.startsWith("R"))
				{
					userch="ROCK";
				}
				else
				{
				userch="PAPER";
				}
				System.out.println(name+" Chose "+userch+" !");
				int choice=rand.nextInt(3);
				String comch;
				if(choice==1)
				{
					comch="SCISSOR";
				}
				else if(choice==2)
				{
					comch="ROCK";
				}
				else
				{
					comch="PAPER";
				}
				System.out.println("Liam chose "+comch+" !");
			
				
				if(userch.equals("SCISSOR"))
				{
					if(comch.equals("ROCK"))
					{
						computer++;
					}
					else if(userch.equals(comch))
					{
						System.out.println("It was a Tie . Try Again");
					}
					else
						user++;
				}
				if(userch.equals("ROCK"))
				{
					if(comch.equals("SCISSOR"))
					{
						user++;
					}
					else if(userch.equals(comch))
					{
						System.out.println("It was a Tie . Try Again");
					}
					else
						computer++;
				}
				if(userch.equals("PAPER"))
				{
					if(comch.equals("SCISSOR"))
					{
						computer++;
					}
					else if(userch.equals(comch))
					{
						System.out.println("It was a Tie . Try Again");
					}
					else
						user++;
				}
				System.out.println("Score :::: "+user+"  -  "+computer);
				if(user==5)
				{
					celebrate();
					System.out.print("PLAY AGAIN?");
					again=input.next();
					if(again.startsWith("y")||again.startsWith("Y"))
					{
						user=0;
						computer=0;
					}
					else
						return;
				}
				if(computer==5)
				{
					mourn();
					System.out.print("PLAY AGAIN?");
					again=input.next();
					if(again.startsWith("y")||again.startsWith("Y"))
					{
						user=0;
						computer=0;
					}
					else
						return;
				}
				
			}
			
		}

	}
		public static void intro()
		{
			System.out.println("Welcome to the game of Scissor- Paper - Rock !!!");
			System.out.print("Enter your Name ---->  ");
			name = input.next();
			name=name.toUpperCase();
			System.out.println("Hye "+name+" ! Do you want to see the Rules?");
			String yn=input.next();
			if(yn.startsWith("y")||yn.startsWith("Y"))
				rules();
			System.out.println("Lets' Play !!!");
			
		}
		public static void rules()
		{
			System.out.println("Liam: \"Hye "+name+" I am Liam! I will be your Rival in this Game.\"");
			System.out.println("Rules-\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+");
			System.out.println("Liam : \"The game has three entities, namely SCISSOR, PAPER and ROCK.");
			System.out.println("You'll have to choose one of the three! I will choose one of three Psuedo-Simultaneously.\n");
			System.out.println("----> Scissor beats Paper");
			System.out.println("----> Paper beats Rock ");
			System.out.println("----> Rock beats Scissor\n");
			System.out.println("whoever scores 5 points first, Wins!");
			System.out.println("For example : If you choose Scissor and I choose paper, You'll win! But, if , I choose rock, since rock beats Scissor, I will win.");
			System.out.println("\nNOTE that : If both of us choose the same, it will be a tie and not be counted as a victory of either party .");
			System.out.println("So,if Everything is done ,Let's Start our Game.\"");
			System.out.println("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+");
		}
		public static void celebrate()
		{
			System.out.println("Congratulations !!!! YOU WON "+name);
			System.out.println("Your score was : "+user+" !\nWhile Liam halted at : "+computer+" !");
			System.out.println(name+", You are Awesome!!!!");
			System.out.println("Liam : \"if you Don't play Another Game with me.I will look for you. I will Hunt for you. I will Kill you.\"");
			System.out.println("Liam : \"but, if you stay, I won't look for you. i won't try to find you . i won't Kill you.\"");
			
			
		}
		public static void mourn()
		{
			System.out.println("Liam : \"Gotcha!!!!\" ");
			System.out.println("OH NO ! You lost. Remember , Liam is not as easy as he looks. ");
			System.out.println("Dont'worry . Try Again!");
			System.out.println("\"n Los Angeles, it\'s like they jog for two hours a day and then they think they\'re morally right. That\'s when you want to choke people, you know?\"-Liam");
			
		}
}
