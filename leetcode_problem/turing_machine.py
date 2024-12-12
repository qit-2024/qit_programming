class TuringMachine:
    def __init__(self, turing_code):
    
        lines = [line.strip() for line in turing_code.split('\n') if line.strip()]
        
        if lines[0].split(':')[0] == 'name':
            name = lines[0].split(':')[1].strip()
        else:
            raise Exception("name is missing") 
    
        if lines[1].split(':')[0] == 'init':
           start_state = lines[1].split(':')[1].strip()
        else:
            raise Exception("init is missing") 
        
        if lines[2].split(':')[0] == 'accept':
              accept_state = lines[2].split(':')[1].strip()
        else:
            raise Exception("accept is missing") 



        transition_function = {}

        try:
                

            for i in range(3, len(lines), 2):
                current_line = lines[i].split(',')
                current_state = current_line[0]
                current_symbol = current_line[1]
                
                next_line = lines[i+1].split(',')
                
                if len(next_line) == 1:
                    next_state = next_line[0]
                    write_symbol = current_symbol
                    move_direction = '>'  # default to right if not specified
                elif len(next_line) == 2:
                    if next_line[1] in ['>', '<', '-']:
                        next_state = next_line[0]
                        write_symbol = current_symbol
                        move_direction = next_line[1]
                    else:
                        next_state = next_line[0]
                        write_symbol = next_line[1]
                        move_direction = '>'  # default to right
                elif len(next_line) == 3:
                
                    next_state = next_line[0]
                    write_symbol = next_line[1]
                    move_direction = next_line[2]
                
                transition_function[(current_state, current_symbol)] = (
                    next_state, 
                    write_symbol, 
                    move_direction
                )
        except:
            raise Exception("Code excecution error") 
        
        self.name = name
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = 'reject'
        self.transition_function = transition_function
        self.blank_symbol = '_'
    
    def simulate(self, input_string):
        """
        Simulate the Turing machine on the given input string
        
        :param input_string: Input to be processed
        :return: Boolean indicating whether input is accepted
        """
        # Initialize tape with input string and blank symbols
        tape = list(input_string)
        
        # Extend tape with blank symbols
        tape.append(self.blank_symbol)
        
        # Current head position starts at the beginning of the tape
        head_position = 0
        
        # Current state starts at the initial state
        current_state = self.start_state
        
        # Step counter to prevent infinite loops
        max_steps = 1000
        steps = 0
        
        # Detailed trace of the machine's computation
        computation_trace = []
        
        while steps < max_steps:
            # If we're beyond the tape, extend it with blank symbol
            if head_position >= len(tape):
                tape.append(self.blank_symbol)
            if head_position < 0:
                tape.insert(0, self.blank_symbol)
                head_position+=1
            
            # Current symbol under the head
            current_symbol = tape[head_position]
            
            # Try to find a transition
            transition_key = (current_state, current_symbol)
            
            # If no transition is defined, move to reject state
            if transition_key not in self.transition_function:
                current_state = self.reject_state
                break
            
            # Get the transition rule
            new_state, write_symbol, move_direction = self.transition_function[transition_key]
            
            # Record this step in the trace
            computation_trace.append({
                'state': current_state,
                'symbol': current_symbol,
                'head_position': head_position,
                'new_state': new_state,
                'write_symbol': write_symbol,
                'move_direction': move_direction
            })
            
            # Write new symbol to tape
            tape[head_position] = write_symbol
            
            # Move head based on direction
            if move_direction == '>':
                head_position += 1
            elif move_direction == '<':
                head_position = head_position - 1
            
            # Update current state
            current_state = new_state
            
            # Check if we've reached accept or reject state
            if current_state == self.accept_state:
                return current_state, computation_trace, tape
            elif current_state == self.reject_state:
                return current_state, computation_trace, tape
            
            steps += 1
        
        # If we've exceeded max steps, reject
        return self.reject_state, computation_trace, tape

def print_computation_trace(trace):
    """
    Print a detailed trace of the Turing machine's computation
    
    :param trace: List of computation steps
    """
    print("Computation Trace:")
    for i, step in enumerate(trace):
        print(f"Step {i}:")
        for key, value in step.items():
            print(f"  {key}: {value}")
        print()

# Example usage: Binary increment
def create_binary_increment_machine():
    return TuringMachine(
        turing_code="""
name: Even amount of zeros
init: q0
accept: qAccept

q0,0
q1,0,>

q1,0
q0,0,>

q0,1
q0,1,>

q1,1
q1,1,>

q0,_
qAccept,_,-"""
    )

# Demonstrate the Turing machine
def main():
    # Create binary increment Turing machine
    tm = create_binary_increment_machine()
    
    # Test cases
    test_inputs = ['0', '1', '11', '101']
    
    for input_str in test_inputs:
        print(f"\nTesting input: {input_str}")
        accepted, trace, tape = tm.simulate(input_str)
        print(f"\nTesting input: {tape}")

        print(f"Input {'accepted' if accepted else 'rejected'}")
        print_computation_trace(trace)

if __name__ == "__main__":
    main()