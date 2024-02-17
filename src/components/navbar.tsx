import { Box, Flex, Text, Link, Image } from "@chakra-ui/react";
import "../style/animated-link.css";

const Navbar = () => {
  return (
    <Flex
      justify="space-between"
      align="center"
      p={6}
      bg="transparent"
      position="fixed"
      width="full"
      zIndex="banner"
      color="white"
    >
      <Link
        href="/"
        _hover={{
          color: "gray", 
          textDecoration: "none", 
        }}
        mx={2}
      >
        SciSketch
      </Link>

      <Box>
        <Link
          href="/abstract-generation"
          _hover={{
            color: "gray", 
            textDecoration: "none",
          }}
          mx={5}
        >
          Abstract Generation
        </Link>
        <Link
          href="/experiment-generation"
          _hover={{
            color: "gray", 
            textDecoration: "none", 
          }}
          mx={2}
        >
          Experiment Generation
        </Link>
      </Box>
    </Flex>
  );
};

export default Navbar;
