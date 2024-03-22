### Policy-Gradient Algorithm

 Policy gradient methods are policy iterative method that means modelling and optimising the policy directly.

 Policy gradient algorithm is a policy iteration approach where policy is directly manipulated to reach the optimal policy that maximises the expected return. 

 This algorithm is model free meaning there are no prior knowledge of the model of the environment. - We do not know the dynamics or the transition probabilities. 

 **Transistion Probability**
 $$ p(s_{t+1} | s, a)$$
 - the probability of reaching the next state $s_{t+1}$ by taking the action from the current state $s$. 

**Policy $\pi$**
$$\pi(a|s)$$


Source: 

[REINFORCE — a policy-gradient based reinforcement Learning algorithm](https://medium.com/intro-to-artificial-intelligence/reinforce-a-policy-gradient-based-reinforcement-learning-algorithm-84bde440c816)